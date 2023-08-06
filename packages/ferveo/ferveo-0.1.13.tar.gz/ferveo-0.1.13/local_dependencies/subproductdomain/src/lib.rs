#![allow(non_snake_case)]
#![allow(dead_code)]

use std::mem;

use ark_ec::{
    pairing::Pairing, scalar_mul::fixed_base::FixedBase, AffineRepr, CurveGroup,
};
use ark_ff::{FftField, Field, Zero};
use ark_poly::{
    univariate::DensePolynomial, DenseUVPolynomial, EvaluationDomain,
    Polynomial, Radix2EvaluationDomain,
};

/// Compute a fast multiexp of many scalars times the same base
/// Only convenient for when called once with given base; if called
/// more than once, it's faster to save the generated window table
pub fn fast_multiexp<Group: CurveGroup>(
    scalars: &[Group::ScalarField],
    base: Group,
) -> Vec<Group::Affine> {
    let window_size = FixedBase::get_mul_window_size(scalars.len());

    let scalar_bits: usize = mem::size_of::<Group::ScalarField>() * 8 - 1;
    let base_table =
        FixedBase::get_window_table(scalar_bits, window_size, base);

    let exp =
        FixedBase::msm::<Group>(scalar_bits, window_size, &base_table, scalars);
    Group::normalize_batch(&exp)
}

#[allow(dead_code)]
pub fn poly_from_scalar<F: FftField>(s: &F) -> DensePolynomial<F> {
    DensePolynomial::<F> { coeffs: vec![*s] }
}

#[allow(dead_code)]
pub fn moduli_from_scalar<F: FftField>(s: &F) -> DensePolynomial<F> {
    DensePolynomial::<F> {
        coeffs: vec![-*s, F::one()],
    }
}

/// Where indicated, algorithms are from Modern Computer Algebra, 3rd edition, by Gathen and Gerhard
/// Abbreviated as GG
/// Let M(n) denote the time to multiply.

/// GG Algorithm 9.3
/// Computes the inverse of f mod x^l
/// Takes O(M(l)) field arithmetic operations
pub fn inverse_mod_xl<F: FftField>(
    func: &DensePolynomial<F>,
    length: usize,
) -> Option<DensePolynomial<F>> {
    let log = ark_std::log2(length); // Compute ceil(log_2(l))
    if let Some(f_0_inv) = func.coeffs[0].inverse() {
        // Invert f(0)^-1 if possible
        let mut func_inv = DensePolynomial::<F> {
            coeffs: vec![f_0_inv], // Constant polynomial f(0)^-1
        };

        let mut acc = 2usize;
        // Use Newton iteration which converges to the inverse mod x^l
        for _ in 0..log {
            func_inv =
                &(&func_inv + &func_inv) - &(func * &(&func_inv * &func_inv)); //TODO: is func_inv*2 better than func_inv+func_inv?
            func_inv.coeffs.resize(
                ark_std::cmp::min(func_inv.coeffs.len(), acc),
                F::zero(),
            ); // Take func_inv remainder mod x^{2^i}
            acc *= 2;
        }
        Some(func_inv)
    } else {
        // No inverse exists because f(0)^-1 does not exist
        None
    }
}

/// GG chapter 9.1
/// Computes the rev_m(f) function in place
/// rev_m(f) = x^m f(1/x)
pub fn rev<F: FftField>(f: &mut DensePolynomial<F>, m: usize) {
    assert!(f.coeffs.len() - 1 <= m);
    for _ in 0..(m - (f.coeffs.len() - 1)) {
        f.coeffs.push(F::zero());
    }
    f.reverse();
}

/// GG Algorithm 9.5
/// Divide f by g in nearly linear time
pub fn fast_divide_monic<F: FftField>(
    func: &DensePolynomial<F>,
    divisor: &DensePolynomial<F>,
) -> (DensePolynomial<F>, DensePolynomial<F>) {
    //TODO: check monic condition

    if func.coeffs().len() < divisor.coeffs().len() {
        return (
            DensePolynomial::<F> {
                coeffs: vec![F::zero()],
            },
            func.clone(),
        );
    }
    let deg_diff = func.coeffs().len() - divisor.coeffs().len();

    let mut rev_f = func.clone();
    let mut rev_g = divisor.clone();
    rev_f.reverse();
    rev_g.reverse();

    let mut quotient =
        &rev_f * &inverse_mod_xl::<F>(&rev_g, deg_diff + 1).unwrap();
    quotient.coeffs.resize(deg_diff + 1, F::zero());
    rev::<F>(&mut quotient, deg_diff);
    let remainder = func - &(divisor * &quotient);
    (quotient, remainder)
}

/// A subproduct domain is a domain { u_0, ..., u_{n-1} } of scalar values
/// accompanied by a subproduct tree of the polynomial:
/// m = (x - u_0)*...*(x-u_{n-1})
/// Once the subproduct tree is constructed, operations over the
/// entire subproduct domain can be done in a fast, recursive way.
/// Unlike other fast algorithms, the subproduct domain may be
/// arbitrary points instead of a multiplicative subgroup
/// of roots of unity of the field
#[derive(Debug, Clone)]
pub struct SubproductDomain<F: FftField> {
    /// Domain values u = { u_0, ..., u_{n-1} }
    pub u: Vec<F>,
    /// Subproduct tree over domain u
    pub t: SubproductTree<F>,
    /// Derivative of the subproduct polynomial
    pub prime: DensePolynomial<F>, // Derivative of the polynomial m
}

impl<F: FftField> SubproductDomain<F> {
    /// Create a new subproduct tree domain over the domain { u_0, ..., u_{n-1} }
    pub fn new(u: Vec<F>) -> SubproductDomain<F> {
        let t = SubproductTree::new(&u);
        let prime = derivative::<F>(&t.m);
        SubproductDomain { u, t, prime }
    }

    #[allow(dead_code)]
    /// Evaluate a polynomial f over the subproduct domain u
    pub fn evaluate(&self, f: &DensePolynomial<F>) -> Vec<F> {
        let mut evals = vec![F::zero(); self.u.len()];
        self.t.evaluate(f, &self.u, &mut evals);
        evals
    }

    #[allow(dead_code)]
    /// Interpolate a polynomial f over the domain, such that f(u_i) = v_i
    pub fn interpolate(&self, v: &[F]) -> DensePolynomial<F> {
        self.t.interpolate(&self.u, v)
    }

    /// Compute the inverse of the lagrange coefficients necessary to interpolate over u
    pub fn inverse_lagrange_coefficients(&self) -> Vec<F> {
        self.t.inverse_lagrange_coefficients(&self.u)
    }

    #[allow(dead_code)]
    /// Compute a linear combination of lagrange factors times c_i
    pub fn linear_combine(&self, c: &[F]) -> DensePolynomial<F> {
        self.t.linear_combine(&self.u, c)
    }
}

/// A subproduct tree of the subproduct domain
/// This type is defined separately from SubproductDomain
/// because the domain u is owned by SubproductDomain, whereas
/// m = (x - u_i)*...*(x-u_j) is owned by the SubproductTree
/// The subdomain { u_i, ..., u_j } is borrowed by SubproductTree for each operation
#[derive(Debug, Clone)]
pub struct SubproductTree<F: FftField> {
    /// The left child SubproductTree
    pub left: Option<Box<SubproductTree<F>>>,
    /// The right child SubproductTree
    pub right: Option<Box<SubproductTree<F>>>,
    /// The polynomial m = (x - u_i)*...*(x-u_j) for this subdomain
    pub m: DensePolynomial<F>,
}

impl<F: FftField> SubproductTree<F> {
    /// GG Algorithm 10.3
    /// Compute the subproduct tree of m = (x - u_0)*...*(x-u_{n-1})
    /// Takes O(M(r) log r) field operations
    /// Specialized to assume the leaves are of the form m_i = x-u_i
    /// Generalized to arbitrary r, not just powers of 2
    pub fn new(u: &[F]) -> SubproductTree<F> {
        // A degree 1 polynomial is a leaf of the tree
        if u.len() == 1 {
            SubproductTree {
                left: None,
                right: None,
                m: DensePolynomial::<F> {
                    coeffs: vec![-u[0], F::one()], // m_0 = x - u_0
                },
            }
        } else {
            // Split as evenly as possible
            let n = u.len() / 2;
            let (u_0, u_1) = u.split_at(n);
            let left = Box::new(SubproductTree::new(u_0));
            let right = Box::new(SubproductTree::new(u_1));
            let m = &left.m * &right.m;
            SubproductTree {
                left: Some(left),
                right: Some(right),
                m,
            }
        }
    }
    /// GG algorithm 9.5
    /// Evaluate f over this subproduct tree
    /// deg(f) must be less than the size of the domain
    /// self must be the subproduct tree of the slice u
    /// The output is stored in the slice t:
    /// t_i = f(u_i)
    /// Takes O(M(n) log n) field operations
    pub fn evaluate(&self, f: &DensePolynomial<F>, u: &[F], t: &mut [F]) {
        assert!(f.degree() < u.len());

        if u.len() == 1 {
            // By the assertion above, f must be a constant polynomial, so evaluating
            t[0] = f.coeffs[0];
            return;
        }

        // if u.len() > 1, then this SubproductTree must not be a leaf, and it has both children
        let left = self.left.as_ref().unwrap();
        let right = self.right.as_ref().unwrap();

        // if f = q*m + r, then on the domain u where m(u_i) = 0, f(u_i) = r(u_i)
        let (_, r_0) = fast_divide_monic::<F>(f, &left.m);
        let (_, r_1) = fast_divide_monic::<F>(f, &right.m);

        // divide the domain in the same way that the SubproductTree was constructed
        let n = u.len() / 2;
        let (u_0, u_1) = u.split_at(n);
        let (t_0, t_1) = t.split_at_mut(n);

        left.evaluate(&r_0, u_0, t_0);
        right.evaluate(&r_1, u_1, t_1);
    }

    #[allow(dead_code)]
    /// Fast interpolate over this subproduct tree
    pub fn interpolate(&self, u: &[F], v: &[F]) -> DensePolynomial<F> {
        let mut lagrange_coeff = self.inverse_lagrange_coefficients(u);

        for (s_i, v_i) in lagrange_coeff.iter_mut().zip(v.iter()) {
            *s_i = s_i.inverse().unwrap() * *v_i;
        }

        self.linear_combine(u, &lagrange_coeff)
    }

    /// Fast compute lagrange coefficients over this subproduct tree
    pub fn inverse_lagrange_coefficients(&self, u: &[F]) -> Vec<F> {
        //assert u.len() == degree of s.m
        if u.len() == 1 {
            return vec![F::one()];
        }
        let mut evals = vec![F::zero(); u.len()];
        let m_prime = derivative::<F>(&self.m);
        self.evaluate(&m_prime, u, &mut evals);
        evals
    }

    #[allow(dead_code)]
    /// GG Algorithm 10.9
    /// Fast linear combination of moduli over this subproduct tree
    /// On input c = { c_0, ..., c_{n-1} }
    /// output sum_i (c_i * m) / (x- u_i)
    /// Takes O(M(n) log n) field operations
    pub fn linear_combine(&self, u: &[F], c: &[F]) -> DensePolynomial<F> {
        if u.len() == 1 {
            // Output c_0 * (x-u_0) / (x-u_0) = c_0
            return DensePolynomial::<F> { coeffs: vec![c[0]] };
        }
        let n = u.len() / 2;
        let (u_0, u_1) = u.split_at(n);
        let (c_0, c_1) = c.split_at(n);

        // Linear combination of moduli over both halves of the subproduct tree
        let left = self.left.as_ref().unwrap();
        let right = self.right.as_ref().unwrap();
        let r_0 = left.linear_combine(u_0, c_0);
        let r_1 = right.linear_combine(u_1, c_1);

        // r_0 = sum_{i in left} c_i m_left / (x-u_i)
        // so m_right * r_0 = sum_{i in left} c_i (m_left*m_right) / (x-u_i) = sum_{i in left} c_i m / (x-u_i)
        &(&right.m * &r_0) + &(&left.m * &r_1)
    }
}

/// Compute the derivative of polynomial f
pub fn derivative<F: FftField>(f: &DensePolynomial<F>) -> DensePolynomial<F> {
    let mut coeffs = Vec::with_capacity(f.coeffs().len() - 1);
    for (i, c) in f.coeffs.iter().enumerate().skip(1) {
        coeffs.push(F::from(i as u128) * c);
    }
    DensePolynomial::<F> { coeffs }
}

/// Build a vector representation of the (n x n) circulant matrix of polynomial f
/// Based on the blog post:
/// https://alinush.github.io/2020/03/19/multiplying-a-vector-by-a-toeplitz-matrix.html
pub fn build_circulant<F: FftField>(
    f: &DensePolynomial<F>,
    n: usize, // Build a 2n x 2n circulant matrix
) -> Vec<F> {
    assert!(n >= f.degree());
    let mut circulant = vec![F::zero(); 2 * n];
    let coeffs = f.coeffs();
    if n == coeffs.len() - 1 {
        circulant[0] = *coeffs.last().unwrap();
        circulant[n] = *coeffs.last().unwrap();
        circulant[n + 1..n + 1 + coeffs.len() - 2]
            .copy_from_slice(&coeffs[1..coeffs.len() - 1]);
    } else {
        circulant[n + 1..n + 1 + coeffs.len() - 1]
            .copy_from_slice(&coeffs[1..]);
    }
    circulant
}

#[allow(dead_code)]
/// Computes the Toeplitz matrix of polynomial times the vector v
pub fn toeplitz_mul<E: Pairing, const NORMALIZE: bool>(
    polynomial: &DensePolynomial<E::ScalarField>,
    v: &[E::G1Affine],
    size: usize,
) -> Result<(Vec<E::G1>, E::ScalarField), anyhow::Error> {
    let m = polynomial.coeffs.len() - 1;
    let size = ark_std::cmp::max(size, m);

    let domain = Radix2EvaluationDomain::<E::ScalarField>::new(2 * size)
        .ok_or_else(|| {
            anyhow::anyhow!("toeplitz multiplication on too large a domain")
        })?;

    let circulant_size = domain.size();
    let toeplitz_size = circulant_size / 2;
    let mut circulant =
        build_circulant::<E::ScalarField>(polynomial, toeplitz_size);

    let mut tmp: Vec<E::G1> = Vec::with_capacity(circulant_size);

    for _ in 0..(toeplitz_size - v.len()) {
        tmp.push(E::G1::zero());
    }

    for i in v.iter().rev() {
        tmp.push(i.into_group());
    }

    tmp.resize(circulant_size, E::G1::zero());
    domain.fft_in_place(&mut tmp);
    domain.fft_in_place(&mut circulant);

    for (i, j) in tmp.iter_mut().zip(circulant.iter()) {
        *i *= *j;
    }

    // NOTE: it is possible to avoid scaling by domain_size_inv, and defer this to later
    domain.ifft_in_place(&mut tmp);

    Ok((
        tmp[..toeplitz_size].to_vec(),
        E::ScalarField::from(domain.size() as u128)
            .inverse()
            .unwrap(),
    ))
}

#[cfg(test)]
mod tests {
    use ark_ec::pairing::Pairing;
    use ark_ff::{One, Zero};
    use ark_poly::{polynomial::univariate::DensePolynomial, Polynomial};
    use ark_std::UniformRand;

    use super::*;

    type ScalarField = <ark_bls12_381::Bls12_381 as Pairing>::ScalarField;
    #[test]
    fn test_inverse() {
        let rng = &mut ark_std::test_rng();

        for l in [1, 2, 3, 5, 19, 25, 101].iter() {
            for degree in 0..(l + 4) {
                for _ in 0..10 {
                    let p = DensePolynomial::<ScalarField>::rand(degree, rng);
                    let p_inv = inverse_mod_xl::<ScalarField>(&p, *l).unwrap();
                    let mut t = &p * &p_inv; // p * p^-1
                    t.coeffs.resize(*l, ScalarField::zero()); // mod x^l
                    assert_eq!(t.coeffs[0], ScalarField::one()); // constant term == 1
                    for i in t.iter().skip(1) {
                        assert_eq!(*i, ScalarField::zero()); // all other terms == 0
                    }
                }
            }
        }
    }

    #[test]
    fn test_divide() {
        let rng = &mut ark_std::test_rng();

        let degree = 100;
        for g_deg in 1..100 {
            let f = DensePolynomial::<ScalarField>::rand(degree, rng);
            let mut g = DensePolynomial::<ScalarField>::rand(g_deg, rng);
            *g.last_mut().unwrap() = ScalarField::one(); //monic

            let (q, r) = fast_divide_monic::<ScalarField>(&f, &g);

            let t = &(&q * &g) + &r;

            for (i, j) in t.coeffs.iter().zip(f.coeffs.iter()) {
                assert_eq!(*i, *j);
            }
        }
    }

    #[test]
    fn test_interpolate() {
        let rng = &mut ark_std::test_rng();
        for d in 1..100 {
            let mut points = vec![];
            let mut evals = vec![];
            for _ in 0..d {
                points.push(ScalarField::rand(rng));
                evals.push(ScalarField::rand(rng));
            }

            let s = SubproductDomain::<ScalarField>::new(points);
            let p = s.interpolate(&evals);

            for (x, y) in s.u.iter().zip(evals.iter()) {
                assert_eq!(p.evaluate(x), *y)
            }
        }
    }

    #[test]
    fn test_linear_combine() {
        let rng = &mut ark_std::test_rng();
        for d in 1..100 {
            let mut u = vec![];
            let mut c = vec![];
            for _ in 0..d {
                u.push(ScalarField::rand(rng));
                c.push(ScalarField::rand(rng));
            }
            let s = SubproductDomain::<ScalarField>::new(u);
            let f = s.linear_combine(&c);

            let r = ScalarField::rand(rng);
            let m = s.t.m.evaluate(&r);
            let mut total = ScalarField::zero();
            for (u_i, c_i) in s.u.iter().zip(c.iter()) {
                total += m * *c_i / (r - u_i);
            }
            assert_eq!(f.evaluate(&r), total);
        }
    }

    #[test]
    fn test_inv_lagrange() {
        let rng = &mut ark_std::test_rng();
        for d in 1..100 {
            let mut u = vec![];
            for _ in 0..d {
                u.push(ScalarField::rand(rng));
            }
            let s = SubproductDomain::<ScalarField>::new(u);
            let f = s.inverse_lagrange_coefficients();

            for (i, j) in s.u.iter().zip(f.iter()) {
                assert_eq!(s.prime.evaluate(i), *j);
            }
        }
    }
}

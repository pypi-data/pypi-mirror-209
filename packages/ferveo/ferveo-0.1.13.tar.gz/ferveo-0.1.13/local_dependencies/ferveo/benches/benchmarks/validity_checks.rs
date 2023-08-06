#![allow(clippy::redundant_closure)]
#![allow(clippy::unit_arg)]

use std::str::FromStr;

use ark_bls12_381::Bls12_381;
pub use ark_bls12_381::Bls12_381 as EllipticCurve;
use criterion::{black_box, criterion_group, BenchmarkId, Criterion};
use digest::crypto_common::rand_core::SeedableRng;
use ferveo::*;
use rand::prelude::StdRng;

const NUM_SHARES_CASES: [usize; 5] = [4, 8, 16, 32, 64];

// TODO: Can we expose ferveo test methods to reuse `setup_dkg` et al instead of reimplementing it here?

fn gen_keypairs(num: u32) -> Vec<ferveo_common::Keypair<EllipticCurve>> {
    let rng = &mut ark_std::test_rng();
    (0..num)
        .map(|_| ferveo_common::Keypair::<EllipticCurve>::new(rng))
        .collect()
}

pub fn gen_address(i: usize) -> EthereumAddress {
    EthereumAddress::from_str(&format!("0x{:040}", i)).unwrap()
}

fn gen_validators(
    keypairs: &[ferveo_common::Keypair<EllipticCurve>],
) -> Vec<Validator<EllipticCurve>> {
    (0..keypairs.len())
        .map(|i| Validator {
            address: gen_address(i),
            public_key: keypairs[i].public(),
        })
        .collect()
}

fn setup_dkg(
    validator: usize,
    shares_num: u32,
) -> PubliclyVerifiableDkg<EllipticCurve> {
    let keypairs = gen_keypairs(shares_num);
    let validators = gen_validators(&keypairs);
    let me = validators[validator].clone();
    PubliclyVerifiableDkg::new(
        &validators,
        &DkgParams {
            tau: 0,
            security_threshold: shares_num / 3,
            shares_num,
        },
        &me,
    )
    .expect("Setup failed")
}

fn setup(
    shares_num: u32,
    rng: &mut StdRng,
) -> (PubliclyVerifiableDkg<Bls12_381>, Message<Bls12_381>) {
    let mut transcripts = vec![];
    for i in 0..shares_num {
        let mut dkg = setup_dkg(i as usize, shares_num);
        transcripts.push(dkg.share(rng).expect("Test failed"));
    }
    let dkg = setup_dkg(0, shares_num);
    let transcript = transcripts[0].clone();
    (dkg, transcript)
}

pub fn bench_verify_full(c: &mut Criterion) {
    let mut group = c.benchmark_group("PVSS VALIDITY CHECKS");
    group.sample_size(10);

    let rng = &mut StdRng::seed_from_u64(0);

    for shares_num in NUM_SHARES_CASES {
        let (dkg, transcript) = setup(shares_num as u32, rng);
        let transcript = &transcript;

        let pvss_verify_optimistic = {
            move || {
                if let Message::Deal(ss) = transcript {
                    black_box(ss.verify_optimistic());
                } else {
                    panic!("Expected Deal");
                }
            }
        };
        let pvss_verify_full = {
            move || {
                if let Message::Deal(ss) = transcript {
                    black_box(ss.verify_full(&dkg));
                } else {
                    panic!("Expected Deal");
                }
            }
        };

        group.bench_function(
            BenchmarkId::new("pvss_verify_optimistic", shares_num),
            |b| b.iter(|| pvss_verify_optimistic()),
        );
        group.bench_function(
            BenchmarkId::new("pvss_verify_full", shares_num),
            |b| b.iter(|| pvss_verify_full()),
        );
    }
}

criterion_group!(validity_checks, bench_verify_full);

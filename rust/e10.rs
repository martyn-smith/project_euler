/*
the sum of all primes up to two million.
*/
mod primegen;

fn euler_10() -> usize {
    let n = 2_000_000;
    primegen::primes_by_sieve(n).iter().sum()
}

fn main() {
    println!("{}", euler_10());
}
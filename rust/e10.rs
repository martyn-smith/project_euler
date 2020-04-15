/*
the sum of all primes up to two million.
*/
mod primegen;
//should return 142913828922.  Instead returns 142969821312, aka 55992390 too high.
fn euler_10() -> isize {
    let n = 2_000_000;
    primegen::primes_by_sieve(n).iter().sum()
}

fn main() {
    println!("{}", euler_10());
}
/*
Finds the largest prime factor of the number 600851475143.
*/
mod primegen;

fn euler_3(big_num : usize) -> usize {
    //find largest prime factor
    let upper_limit = (big_num as f64).sqrt().ceil() as usize;
    let primes = primegen::primes_by_sieve(upper_limit);
    *primes.iter().filter(|&p| big_num % p == 0).max().unwrap()
}

fn main() {
    println!("{}", euler_3(600_851_475_143));
}
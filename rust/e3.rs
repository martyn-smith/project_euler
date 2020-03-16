/*
Finds the largest prime factor of the number 600851475143.
*/

fn primes_by_sieve(max_num : usize) -> Vec<isize> {
    let mut sieve vec![true; max_num];
    let mut primes : Vec<isize> = vec![];
    for i in 2..sieve.len() {
        if sieve[i] { //is prime
            primes.push(i);
            for j in 2..sieve.len() / i {
                sieve[j * i] = false;
                j += 1;
            }
        }
    }
    primes
}


fn euler_3(big_prime : isize) -> isize {
    //find largest prime factor
    let upper_limit = (big_prime as f64).sqrt().ceil() as usize;
    let primes = primes_by_sieve(upper_limit);
    let mut biggest_factor = 0;
    loop {

    }
    biggest_factor
}

fn main() {
    println!("{}", euler_3(600851475143));
}
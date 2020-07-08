#![allow(dead_code)]

//when tested with n=2_000_000 and for loop, first flaw is 1999117, product of 947 and 2111
pub fn primes_by_sieve(max_num : isize) -> Vec<isize> {
    let mut sieve = vec![true; max_num as usize];
    let mut primes : Vec<isize> = vec![];
    let mut j: usize;
    for i in 2..sieve.len() {
        if sieve[i] { //is prime
            primes.push(i as isize);
            j = 2;
            //for j in 2..=sieve.len() / i //omitted as couldn't get the offsets to work.
            while i*j < sieve.len() { 
                sieve[i * j] = false;
                j += 1;
            }
        }
    }
    primes
}

fn is_prime(candidate : usize, primes: &Vec<usize>) -> bool {
    let mut is_prime = false;
    while !is_prime {
        is_prime = true;
        for prime in primes {
            if candidate % prime == 0 {
                is_prime = false;
                break;
            }
        }
    }
    is_prime
}

// impl next_prime for Vec<usize> {
    
// }

pub fn nth_prime(n: usize) -> usize {
    let mut primes : Vec<usize> = vec![2];
    let mut candidate : usize;
    while primes.len() < n {
        candidate = *primes.last().unwrap() + 1;
        while primes.iter()
                  .filter(|&i| candidate % i == 0)
                  .collect::<Vec<&usize>>()
                  .len() > 0 {
            candidate += 1;
        }
        primes.push(candidate);
    }
    *primes.last().unwrap()
}
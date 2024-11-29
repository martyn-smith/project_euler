#![allow(dead_code)]

pub fn primes_by_sieve(m : usize) -> Vec<usize> {
    let mut sieve = vec![true; m as usize];
    let mut primes : Vec<usize> = vec![];
    for i in 2..m {
        if sieve[i] { //is prime
            primes.push(i as usize);
            for j in 2..=((m - 1) / i) {
                sieve[i * j] = false;
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

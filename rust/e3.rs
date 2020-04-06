/*
Finds the largest prime factor of the number 600851475143.
*/

fn primes_by_sieve(max_num : isize) -> Vec<isize> {
    let mut sieve = vec![true; max_num as usize];
    let mut primes : Vec<isize> = vec![];
    for i in 2..sieve.len() {
        if sieve[i] { //is prime
            primes.push(i as isize);
            for j in 2..sieve.len() / i {
                sieve[j * i] = false;
            }
        }
    }
    primes
}

fn euler_3(big_num : isize) -> isize {
    //find largest prime factor
    let upper_limit = (big_num as f64).sqrt().ceil() as isize;
    let primes = primes_by_sieve(upper_limit);
    biggest_factor(&primes, big_num)
}

// fn biggest_factor_functional(primes : Vec<isize>, big_num: isize) -> isize {
//     max()
// }

fn biggest_factor(primes: &Vec<isize>, big_num : isize) -> isize {
    let mut biggest_factor = 0;
    //primes.iter().filter(|p| big_num % *p == 0);
    for p in primes {
        if big_num % *p == 0 {
            biggest_factor = *p;
        }
    }
    biggest_factor
}

fn main() {
    println!("{}", euler_3(600851475143));
}
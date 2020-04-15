/*
Finds the largest prime factor of the number 600851475143.
*/
mod primegen;

fn euler_3(big_num : isize) -> isize {
    //find largest prime factor
    let upper_limit = (big_num as f64).sqrt().ceil() as isize;
    let primes = primegen::primes_by_sieve(upper_limit);
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
    println!("{}", euler_3(600_851_475_143));
}
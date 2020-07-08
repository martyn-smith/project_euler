/*
Finds the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20.

 primes between 0 and 20: 2,3,5,7,11,13,17,19
 - if a number is divisible by these, it is divisible by
   all numbers between 0 and 20

*/

use std::cmp;

fn euler_5() -> usize {
    let n = 20;
    let (mut power, mut base);
    let (mut primes, mut powers) = (vec![2], vec![0]);
    for j in 2..=n {
        base = j;
        for (i, p) in primes.iter().enumerate() {
            power = 0;
            while base % p == 0 {
                power += 1;
                base /= p;
            }
            powers[i] = cmp::max(power, powers[i]);
        }
        if base > 1 { //is prime
            primes.push(base);
            powers.push(1);
        }
    }
    primes.iter()
        .zip(powers.iter())
        .fold(1, |answer, x| answer * (*x.0 as usize).pow(*x.1 as u32) )
}

fn main() {
    println!("{}", euler_5());
}
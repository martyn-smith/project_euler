/*
Finds the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20.

 primes between 0 and 20: 2,3,5,7,11,13,17,19
 - if a number is divisible by these, it is divisible by
   all numbers between 0 and 20

*/

fn euler_5() -> isize {
    let mut candidate = 1;
    //let primes = [2, 3, 5, 7, 11, 13, 17, 19];
    loop {
        if (1..=20).filter(|p| candidate % *p == 0).count() == 20 {
            break;
        }
        candidate += 1;
    }
    candidate
}

fn main() {
    println!("{}", euler_5());
}
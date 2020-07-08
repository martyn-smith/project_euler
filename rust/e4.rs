/*
Find the largest palindrome made from the product of two 3-digit numbers.
*/
use std::cmp;

fn euler_4() -> usize {
    let (mut candidate, mut etadidnac, mut max_palindrome) = (0, 0, 0);
    for i in 100..1000 {
        for j in 100..1000 {
            candidate = i*j;
            etadidnac = reverse(candidate);
            if candidate == etadidnac {
                max_palindrome = cmp::max(max_palindrome, candidate);
            }
        }
    }
    max_palindrome
}

fn reverse(mut num: usize) -> usize {
    let (mut digit, mut mun) = (0, 0);
    while num > 0 {
        digit = num % 10;
        mun *= 10;
        mun += digit;
        num = num / 10;
    }
    mun
}

fn main() {
    println!("{}", euler_4());
}
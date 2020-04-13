use std::cmp;

fn euler_4() -> isize {
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

fn reverse(mut num: isize) -> isize {
    let (mut digit, mut i, mut mun) = (0, 0, 0);
    while num > 0 {
        digit = num % 10;
        mun *= 10;
        mun += digit;
        num = num / 10;
        i += 1;
    }
    mun
}

fn main() {
    println!("{}", euler_4());
}
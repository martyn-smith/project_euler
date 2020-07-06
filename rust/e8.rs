/*
the data file contains a 1000-digit number.
Find the thirteen adjacent digits in the 1000-digit number that have
the greatest product.
*/

use std::cmp;
use std::collections::VecDeque;
use std::fs::File;
use std::io::Read;

const FILENAME : &str = "../data/8.dat";
const BUFFER_LEN : usize = 1000;
const WINDOW_LEN : usize = 13;

fn euler_8() -> usize {
    //verified - or at least python equivalent.
    let mut f = File::open(FILENAME).unwrap();

    // read whole file as ASCII.
    let mut numbers = [0u8; BUFFER_LEN];
    f.read(&mut numbers).unwrap();

    let mut max_product = 0;
    let mut prod : usize;

    //load first thirteen into window and convert to ascii
    let mut window: VecDeque::<u8> = numbers[0..WINDOW_LEN].iter().map(|x| x - 0x30).collect();
    /*cycle through, pushing new element and popping oldest. 
    If product is larger, reassign - we only care about the result.*/
    for i in 0..(BUFFER_LEN - WINDOW_LEN) {
        window.pop_front();
        window.push_back(numbers[i] - 0x30);
        prod = window.iter().fold(1, |prod, val| prod * *val as usize);
        max_product = cmp::max(prod, max_product);
    }
    max_product
}

fn main() {
    println!("{}", euler_8());
}
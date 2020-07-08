/*
the data file contains a 1000-digit number.
Find the thirteen adjacent digits in the 1000-digit number that have
the greatest product.
*/

use std::fs; 

const FILENAME : &str = "../data/8.dat";
const WINDOW_LEN : usize = 13;

fn euler_8() -> usize {
    // verified - or at least python equivalent.
    // read whole file as ASCII and convert.
    let numbers : Vec<u8> = fs::read(FILENAME).unwrap().iter().map(|x| x - 0x30).collect();

    /* Old way: load first thirteen into a queue, then push new/pop last.
       Requires std::collections::VecDeque, std::iter::FromIterator, and std::cmp::max.
       Then I discovered windows() exists.
        // let mut window = VecDeque::from_iter(numbers[0..WINDOW_LEN].iter());
        // for i in 0..(numbers.len() - WINDOW_LEN) {
        //     window.pop_front();
        //     window.push_back(&numbers[i]);
        //     max_product = cmp::max(window.iter().map(|&&x| x as usize).product(), max_product);
        // }
    */
    numbers.windows(WINDOW_LEN)
                .map(|wndw| wndw.iter()
                    .map(|&x| x as usize)
                    .product())
                .max().unwrap()
}

fn main() {
    println!("{}", euler_8());
}
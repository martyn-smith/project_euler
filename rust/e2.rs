/*
Find the sum of even-numbered fibonacci terms below four million.
*/
mod fibonaccigen;
use fibonaccigen::make_list;

fn euler_2(max_num : usize) -> usize {
    let fibonacci_list = make_list(max_num);
    fibonacci_list.into_iter().filter(|&x| x % 2 == 0).sum()
}

fn main() {
    println!("{}", euler_2(4_000_000));
}

#[test]
fn test_euler_2() {
    assert_eq!(euler_2(4_000_000), 4613732);
}
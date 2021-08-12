/*
Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
*/

fn euler_1(max_num : usize) -> usize {
    const FIZZERS: [usize; 2] = [3, 5];
    (0..max_num)
        .filter(|i| FIZZERS.iter()
                           .any(|f| i % f == 0))
        .sum()
}

fn main() {
    println!("{}", euler_1(1000));
}

#[test]
fn test_euler_1() {
    assert_eq!(euler_1(1000), 233168);
}

/*
Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
*/

fn euler_1(max_num : i32) -> i32 {
    let mut total = 0;
    for i in 0..max_num {
        if (i % 3 == 0) || (i % 5 == 0) {
            total += i;
        }
    }
    return total;
}

fn main() {
    println!("{}", euler_1(1000));
}
/*
Find the sum of even-numbered fibonacci terms below four million.
*/
fn fibonacci(&fib_nums) -> i32 {
    let len = fib_nums.len();
    match len {
        0 => return(0),
        1 => return(1),
        _ => return(fib_nums[len -1] + fib_nums[len -2])
    }
}

fn make_fibonacci_list(max_num: i32) -> Vec<i32> {
    let mut f = 0;
    let fib_nums = vec![];
    while 
}

fn euler_2(max_num : i32) -> i32 {
    let mut sum = 0;
    for i in 0..max_num {
        if (i % 2 == 0) {
            sum += i;
        }
    }
    return sum;
}

fn main() {
    println!("{}", euler_2(4_000_000));
}

/*
Find the sum of even-numbered fibonacci terms below four million.
*/
fn fibonacci(fib_list: &Vec<isize>) -> isize {
    let len = fib_list.len();
    match len {
        0 => 0,
        1 => 1,
        _ => fib_list[len -1] + fib_list[len -2]
    }
}

fn make_fibonacci_list(max_num: isize) -> Vec<isize> {
    let mut f;
    let mut fib_list = vec![];
    loop {
        f = fibonacci(&fib_list);
        if f < max_num {
            fib_list.push(f);
        } else {
            break;
        }
    }
    fib_list
}

fn euler_2(max_num : isize) -> isize {
    let fib_list = make_fibonacci_list(max_num);
    fib_list.into_iter().filter(|&x| x % 2 == 0).sum()
}

fn main() {
    println!("{}", euler_2(4_000_000));
}

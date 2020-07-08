fn recursive(n : usize) -> usize {
    match n {
        0 => 0,
        1 => 1,
        _ => recursive(n - 1) + recursive(n - 2)
    }
}

fn iterative(mut n : usize) -> usize {
    let mut seq : [usize; 2] = [0, 1];
    let mut next : usize;

    while n >= 2 {
        next = seq[1] + seq[0];
        seq[0] = seq[1];
        seq[1] = next; 
        n -= 1;
    }
    seq[n]
}

pub fn make_list(max_num: usize) -> Vec<usize> {
    let mut f;
    let mut fib_list = vec![];
    loop {
        f = recursive(fib_list.len());
        if f < max_num {
            fib_list.push(f);
        } else {
            break;
        }
    }
    fib_list
}
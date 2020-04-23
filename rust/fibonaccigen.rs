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
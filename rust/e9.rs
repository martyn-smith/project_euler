/*
There is one pythagorean triple whose sum is 1000 (i.e. a + b + c = 1000, and a^2 = b^2 + c^2.)
Returns the product of that triple.
*/

fn euler_9() -> Option<usize> {
    for a in 1..1000 {
        for b in 1..(1000-a) {
            let c : usize = 1000 - (a + b);
            if a.pow(2) == b.pow(2) + c.pow(2) {
                return Some(a * b * c);
            }
        }
    }
    None
}

fn main() {
    println!("{}", euler_9().expect("no solution found"));
}
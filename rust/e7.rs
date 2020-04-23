mod primegen;

fn euler_7(n: usize) -> usize {
    primegen::nth_prime(n)
}

fn main() {
    println!("{}", euler_7(10_001));
}
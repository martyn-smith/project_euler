
/*
Finds the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

NOTE: the problem ACTUALLY wants the difference between the square of the sum
and the sum of the squares.
*/

fn euler_6_easy_way() -> usize {
    let sum_of_squares: usize = (1..=100).map(|x: usize| x.pow(2)).sum();
    let square_of_sum = (1..=100).sum::<usize>().pow(2);
    square_of_sum - sum_of_squares
}

fn euler_6_better_way() -> usize {
    //uses S_n = n(a_1 + a_n)/2
    //to be honest, I forget how sum_of_squares works...
    //TODO: sum_of_squares needs to be calculated as a float then cast to int
    //..I think.  Probably a better way.
    let sum_of_squares = (1_000_000/3) + (10_000/2) + (100/6); //338350
    let square_of_sum = (100*101/2 as usize).pow(2);
    square_of_sum - sum_of_squares
}

fn main() {
    println!("easy way: {}", euler_6_easy_way());
    println!("better way: {}", euler_6_better_way());
}

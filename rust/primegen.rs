//when tested with n=2_000_000 and for loop, first flaw is 1999117, product of 947 and 2111
pub fn primes_by_sieve(max_num : isize) -> Vec<isize> {
    let mut sieve = vec![true; max_num as usize];
    let mut primes : Vec<isize> = vec![];
    let mut j: usize;
    for i in 2..sieve.len() {
        if sieve[i] { //is prime
            primes.push(i as isize);
            j = 2;
            //for j in 2..=sieve.len() / i //omitted as couldn't get the offsets to work.
            while i*j < sieve.len() { 
                sieve[i * j] = false;
                j += 1;
            }
        }
    }
    primes
}
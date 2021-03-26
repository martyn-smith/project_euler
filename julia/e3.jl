include("primegen.jl")

function euler_3(max_num::Int)::Int
    candidates = primes_by_sieve(isqrt(max_num))
    maximum(filter(c -> max_num % c == 0, candidates))
end

println(euler_3(600851475143))

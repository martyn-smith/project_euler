
include("primegen.jl")

function euler_7(max_num::Int)::Int
   last(collect(Iterators.take(primes_by_trial(), max_num)))
end

println(euler_7(10001))

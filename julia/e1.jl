#= Project Euler problem 1: print the sum of all integers between 1 and 1000 (exclusive),
divisible by 3 or 5. Essentially fizzbuzz++
=#

function euler_1(max_num::Int)::Int
    reduce(+, filter(x -> x % 3 == 0 || x % 5 == 0, range(1, stop=max_num-1)))
end

println(euler_1(1000))

#Find the sum of all even-numbered fibonacci terms below four million.
#as always, the actual fibonacci generation will be in a separate package.

include("fibgen.jl")

function euler_2(max_num::Int)::Int
   sum(filter(x -> x % 2 == 0, collect(Iterators.takewhile(<(max_num), fib()))))
end

println(euler_2(4000000))

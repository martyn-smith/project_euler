#=
Problem six: find the difference between the sum of the squares of the first hundred
natural numbers and the square of the sum.

As previously, the question is worded wrong: it actually wants the opposite.
=#

function euler_6(max_num::Int)::Int
    sum(1:max_num)^2 - sum(map(x -> x^2, 1:max_num)) 
end

println(euler_6(100))

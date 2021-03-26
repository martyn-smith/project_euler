#=
Finds the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20.


 primes between 0 and 20: 2,3,5,7,11,13,17,19
 - if a number is divisible by these, it is divisible by
   all numbers between 0 and 20

=#

function euler_5(n::Int)::Int
    #answer by hand - the product of maximum powers of each prime
    #answer = (2^4)*(3^2)*5*7*11*13*17*19
    (primes, powers) = [2], [0]
    for num in 2:n+1
        for (i, p) in enumerate(primes)
            power = 0
            while num % p == 0
                power += 1
                num ÷= p
            end
            powers[i] = max(power, powers[i])
        end
        if num > 1 #is prime
            push!(primes, num)
            push!(powers, 1)
        end
    end
    #(*, 1, base^powers)
    prod(map((b,p) -> b^p, primes, powers))
end

println(euler_5(20)) 

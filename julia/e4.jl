#=
Find the largest palindrome made from the product of two 3-digit numbers.
=#

function euler_4()::Int
    #verified
    big_palindrome = 0
    for (i, j) in Base.Iterators.product(100:999,100:999)
        candidate = (i*j)
        #we're doing it the hard way, damnit - no tostring() method!
        etadidnac = reverse(candidate)
        if (etadidnac == candidate)
            big_palindrome = max(big_palindrome, candidate)
        end
    end
    big_palindrome
end

function reverse(num::Int)::Int
    i = 0
    mun = 0
    while num > 0
        digit = num % 10
        mun *= 10
        mun += digit
        num ÷= 10
        i += 1
    end
    mun
end

println(euler_4())

function primes_by_sieve(max_num::Int)::Vector{Int}

    nums = trues(max_num)
    primes = []
    
    for i in 2:max_num
        if nums[i]
            push!(primes, i)
            j = 2
            while (i * j) < length(nums)
                nums[i * j] = false
                j += 1
            end
        end
    end
    primes
end

function fib(max_num::Int)
   a, b = 0, 1
   Channel(ctype=Int, csize=1) do c
       while (b < max_num)
           put!(c, b)
           a, b = b, a+b
       end
   end
end

function euler_2(max_num::Int)::Int
   reduce(+, filter(x -> x % 2 == 0, collect(fib(max_num))))
end

print(euler_2(4000000))

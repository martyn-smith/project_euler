#Functions for generating fibonacci sequences.

function fib(max_num::Int)
   a, b = 0, 1
   Channel(ctype=Int, csize=1) do c
       while (b < max_num)
           put!(c, b)
           a, b = b, a+b
       end
   end
end

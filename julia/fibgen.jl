#Functions for generating fibonacci sequences.

function fib()
   a, b = 0, 1
   Channel(ctype=Int, csize=1) do c
        while (true)
            put!(c, b)
            a, b = b, a+b
        end
   end
end

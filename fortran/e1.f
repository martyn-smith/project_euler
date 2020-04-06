! sums all multiples of 3 and 5 between 1 and 1000 (fixed form version)

      program Euler1
      integer :: n, sum = 0
      do 10 i = 1, 999
        if (mod(i, 3) == 0 .or. mod(i, 5) == 0) then 
            n = i
        else 
            n = 0
        end if
10      sum = sum + n
      print *, sum
      end program Euler1

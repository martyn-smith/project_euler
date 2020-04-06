! sums all multiples of 3 and 5 between 1 and 1000

program Euler1
    integer :: sum = 0
    do i = 1, 999
        if (mod(i, 3) == 0 .or. mod(i, 5) == 0) then 
            sum = sum + i
        end if
    end do 
    print *, sum
end program Euler1

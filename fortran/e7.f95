! finds the 10001st prime

program Euler7

    integer, dimension (:), allocatable :: primes
    integer :: candidate, prime
    logical :: is_prime
    allocate(primes(1))
    primes(1) = 2

    do while (ubound(primes) < n - 1)
        candidate = ubound(primes) + 1
        is_prime = .false.
        do while (.not. is_prime)
            is_prime = .true.
            do (p = 0, ubound(primes))
                if (mod(candidate, p) == 0 ) then
                    is_prime = .false.
                    break
                end if
            end do
            if (is_prime) then
                length++
                primes = (int*)realloc(primes, sizeof(int*) * (length + 1))
                ubound(primes) = candidate
            else
                candidate++
            end if
        end do
    end do
    prime = ubound(primes)

    print *, prime
    deallocate(primes)
end program Euler7
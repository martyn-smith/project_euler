int nth_prime(int n) {
    int* primes = (int*)malloc(sizeof(int*));
    int candidate, length = 0;
    bool is_prime;
    primes[0] = 2;
    while (length < n - 1) {
        candidate = primes[length] + 1;
        is_prime = false;
        while (!is_prime) {
            is_prime = true;
            for (int p = 0; p < length; p++) {
                if (candidate % primes[p] == 0){
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) {
                length++;
                primes = (int*)realloc(primes, sizeof(int*) * (length + 1));
                primes[length] = candidate;
            } else {
                candidate++;
            }
        }
    }
    return primes[length];
}
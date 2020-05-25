/*
Find the sum of even-numbered fibonacci terms below four million.
*/
#include <stdlib.h>
#include <stdio.h>
#define MAX_NUM 4000000

int euler_2() {
    // moved OUT of fibonaccigen.  There's not much difficult code,
    // and there is a modification that's difficult to patch in efficiently.
    int sum = 0, seq[3] = {0, 1, NULL}, n = MAX_NUM;
    while (seq[1] < n) {
        seq[2] = seq[1] + seq[0];
        seq[0] = seq[1];
        seq[1] = seq[2];
        if (seq[1] % 2 == 0) {
            sum += seq[1];
        }
    }
    return sum;
}

int main() {
    printf ("%d\n", euler_2());
    return 0;
}
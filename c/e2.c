/*
Find the sum of even-numbered fibonacci terms below four million.
*/
#include <stdio.h>
MAX_NUM = 4000000;

int* fibonaccigen(int max_num) {
    int next, *seq;
    seq[0] = 0;
    seq[1] = 1;
    while (next < max_num) {
        next = seq[-1] + seq[-2];
        //add to linked list
    }
    return seq;
}

int euler_2() {
    int total = 0, *fibonacci;
    *fibonacci = fibonaccigen(MAX_NUM);
    for (int i=0; i<len(fibonacci); i++) {
        total += fibonacci[i];
    }
    return total;
}

int main() {
    printf ("%d", euler_2());
    return 0;
}
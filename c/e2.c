/*
Find the sum of even-numbered fibonacci terms below four million.
*/
#include <stdlib.h>
#include <stdio.h>
#include "fibonaccigen.c"
#define MAX_NUM 4000000

int euler_2() {
    return fibonacci_sum(MAX_NUM);
}

int main() {
    printf ("%d\n", euler_2());
    return 0;
}
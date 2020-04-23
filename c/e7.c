#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include "primegen.c"

int euler_7() {
    return nth_prime(10001);
}

int main() {
    printf ("%d\n", euler_7());
    return 0;
}
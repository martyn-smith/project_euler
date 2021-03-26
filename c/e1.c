/*
Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
*/
#include <stdio.h>
int MAX_NUM = 1000;

int euler_1(int MAX_NUM) {
    int total = 0;
    for (int i=0; i<MAX_NUM; i++) {
        if (!(i % 3) || !(i % 5)) {
            total += i;
        }
    }
    return total;
}

int main() {
    printf ("%d\n", euler_1(1000));
    return 0;
}

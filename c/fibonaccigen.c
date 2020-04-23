#include <stddef.h>

typedef struct lnode {
    struct lnode* next;
    int data;
} lnode;

int len(lnode* l) {
    int i;
    for (i = 0; l->next != NULL; l = l->next) {
        i++;
    }
    return i;
}

lnode* index(lnode* l, int idx) {
    int i;
    while (i < idx) {
        l = l->next;
        i++;
    }
    return l;
}

lnode* fibonaccigen(int max_num) {
    lnode* seq = (lnode*)malloc(sizeof(lnode));
    int i, j;
    seq->data = 0;
    seq->next = (lnode*)malloc(sizeof(lnode));
    seq->next->data = 1;
    while (i < max_num) {
        j = len(seq);
        index(seq, j)->next = (lnode*)malloc(sizeof(lnode));
        index(seq, j)->next->data = index(seq, j-1)->data + index(seq, j-2)->data;
    }
    return seq;
}

/*
fn definition

f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)

*/

int fibonacci_recursive(int n) {
    switch(n) {
        case 0 :
            return 0;
        case 1 :
            return 1;
        default :
            return fibonacci_recursive(n-1) + fibonacci_recursive(n-2);
    }
}

int fibonacci_iterative(int n) {
    int seq[3] = {0, 1, NULL};
    for (; n >= 2; n--) {
        seq[2] = seq[1] + seq[0];
        seq[0] = seq[1];
        seq[1] = seq[2]; 
    }
    return seq[n];
}

int fibonacci_sum(int n) {
    int sum = 0,seq[3] = {0, 1, NULL};
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

/*
matrix mult method:

f(n) = [1 0] [0 1  **n [0
              1 1]      1]
*/

/*
numerical approximation

f(n) = phi**n - psi**n / (phi - psi)

f-1(f) = (phi - psi) * ()

where:

    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2

*/
/*/////////////////////////////////////////////
//   Title:         L3_Q1.c
//   Author:        Ryan L.
//   Description:   returns the numbers between low and high that are divisible by x
*//////////////////////////////////////////////
#include <stdio.h>

int main(){
    // Declare variables (test case: 1 12 2 (2 4 6 8))
    int low, high, x;

    // Initialize variables
        //get input low, high, iterater
    printf(": ");
    scanf("%d %d %d", &low, &high, &x);

    //Work
        //iterate through low to high
    for (int i = low; i < high; i++){

        //if i is a multiple of x, print i
        if (i % x == 0){
            printf("%d, ", i);
        }
    }
    return 0;
}
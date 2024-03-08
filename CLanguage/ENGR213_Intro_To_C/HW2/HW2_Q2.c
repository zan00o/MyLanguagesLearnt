/*/////////////////////////////////////////////
//   Title:         HW2_Q2.c
//   Author:        Ryan L.
//   Description:   C program to calulate the sum of a reaccuring series [(x^n)/n!] and print the result
*//////////////////////////////////////////////
#include <stdio.h>
#include <math.h>

int main(){
    // Declare variables (test case: 3 5 (16.375000))
    int n;
    double x, fac=1, sum = 0;

    // Initialize variables
    printf("Input the value of x: ");
    scanf("%lf", &x);
    printf("Input the number of terms: ");
    scanf("%d", &n);

    //Work
    for(int i = 0; i < n; i++){
        fac *= (i>0)?i:1;
        sum += pow(x,i)/fac;

    }
    printf("%lf",sum);
    return 0;
}
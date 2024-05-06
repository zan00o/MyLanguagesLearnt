/*/////////////////////////////////////////////
//   Title:         HW5_Q1.c
//   Author:        Ryan L.
//   Description:   program to demonstrate the use of &(address of) and *(value at address) operator.
*//////////////////////////////////////////////
#include <stdio.h>

int main(){
    // Declare variables (test case: )
    int a, *pta;      // int
    double b, *ptb;   // float
    char c, *ptc;     // char



    // Initialize variables
    printf("pointer: Demonstrate the use of & and * operator :\n");
    printf("------------------------------------------------------\n");
    // Ask user for the value of a, b, and c
    printf("m = ");
    scanf("%d", &a);

    printf("fx = ");
    scanf("%lf", &b);

    printf("cht = ");
    scanf(" %c", &c);
    

    //Work
    // Print the address of a, b, and c using & operator
    printf("using & operator : \n");
    printf("----------------\n");
    printf("address of a = %p\n", &a);
    printf("address of b = %p\n", &b);
    printf("address of c = %p\n", &c);

    // Print the value at address of a, b, and c using * and & operator
    printf("using & and * operator : \n");
    printf("-------------------------\n");
    printf("value at address of a = %d\n", *&a);
    printf("value at address of b = %f\n", *&b);
    printf("value at address of c = %c\n", *&c);

    // Print the value at address of a, b, and c using only pointer variable
    printf("using only pointer variable : \n");
    printf("---------------------------\n");
    printf("address of a = %p\n", pta);
    printf("address of b = %p\n", pta);
    printf("address of c = %p\n", pta);

    // Print the value at address of a, b, and c using only pointer operator
    printf("using only pointer operator : \n");
    printf("---------------------------\n");
    printf("value at address of a = %d\n", *&a);
    printf("value at address of b = %f\n", *&b);
    printf("value at address of c = %c\n", *&c);


    return 0;
}
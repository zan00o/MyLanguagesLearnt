/*/////////////////////////////////////////////
//   Title:         L2_Q3.c
//   Author:        Ryan L.
//   Description:   C program that prints the lowest of 3 given values
*//////////////////////////////////////////////

#include <stdio.h>

int main(){
    // Declare variables (test cases: 7 15 3)
    int n1, n2, n3;

    // Initialize variables

        //get input for 3 nums
    printf(": ");
    scanf("%d %d %d", &n1, &n2, &n3);

    //find and print the smallest of the 3 numbers

    if ((n1<=n2) && (n1<=n3)){
        printf("%d",n1);

    } else if ((n2<=n1) && (n2<=n3)){
        printf("%d",n2);

    } else {
        printf("%d",n3);

    }
    
    return 0;
}
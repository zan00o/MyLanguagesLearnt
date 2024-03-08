/*/////////////////////////////////////////////
//   Title:      Q4.c           
//   Author:     Ryan L. 
//   Description: Answer to Q4 for HW 1
*/////////////////////////////////////////////

#include <stdio.h>

int main() {
    // declare variables
    int a, b, c, d;

    // prompt user for input
    printf("Input the first integer: ");
    scanf("%d", &a);
    printf("Input the second integer: ");
    scanf("%d", &b);
    printf("Input the third integer: ");
    scanf("%d", &c);
    printf("Input the fourth integer: ");
    scanf("%d", &d);

    // filter using the given conditions 
    // (b > c) && (d > a) && (c + d > a + b)
    if (b > c && d > a && c + d > a + b) {
        printf("Correct values\n");
    } else {
        printf("Wrong values\n");
    }
    return 0;
}
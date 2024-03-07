/*/////////////////////////////////////////////
//   Title:     L1_Q6.c         
//   Author:    Ryan L. 
//   Description: Swapping the values of x & y
*//////////////////////////////////////////////

#include <stdio.h>

int main() {

    //declare needed variables (test case: 5 7)
    int x, y;

    //prompt user for x & y
    printf("Input values for x & y: ");
    scanf("%d %d", &x, &y);

    //print the values of x & y before swapping
    printf("before swapping the values of x & y: %d %d\n", x, y);
    
    //swapping the values
    x = x + y;
    y = x - y;
    x = x - y;
    
    //print the values of x & y after swapping
    printf("after swapping the values of x & y: %d %d\n", x, y);
    
    return 0;
}
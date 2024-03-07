/*/////////////////////////////////////////////
//   Title:     L1_Q3.c
//   Author:    Ryan L. 
//   Description: Calculating the product and average of 4 numbers in both int and double format
*//////////////////////////////////////////////

#include <stdio.h>

int main() {
    // needed variables (test case: 8 10 5 4)
    int num1, num2, num3, num4;

    double avgdbl, proddbl;
    
    //gather input from user
    printf(": ");
    scanf("%d %d %d %d", &num1, &num2, &num3, &num4);
    
    //print the product and average of the numbers
    printf("%d\t%d\n",(num1*num2*num3*num4),(num1+num2+num3+num4)/4);

    //turn the numbers into doubles
    proddbl = num1*num2*num3*num4;
    avgdbl = (num1+num2+num3+num4);
    avgdbl = avgdbl/4;

    //print the product and average of the numbers in double format
    printf("%.3f\t%.3f",proddbl,avgdbl);
    
    return 0;
}
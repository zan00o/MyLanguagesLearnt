/*/////////////////////////////////////////////
//   Title:         L2_Q2.c
//   Author:        Ryan L.
//   Description:   c program that calculates the tax rate from a given annual salary
*//////////////////////////////////////////////

#include <stdio.h>

int main(){
    // Declare variables (test cases: 120000)
    int annulSalary, taxToPay;
    double taxRate;

    // Initialize variables

        //get input: annual salary
    printf("Enter annual salary: ");
    scanf("%d", &annulSalary);

    //calculate taxRate

    if (annulSalary <= 20000) {
        taxRate = 0.10;

    } else if (annulSalary <= 50000) {
        taxRate = 0.20;

    } else {
        taxRate = 0.30;
    }
    
    //calculate the taxToPay

    taxToPay = annulSalary * taxRate;

    //print all needed info
    
    printf("Annual salary:\t%d\n", annulSalary);
    printf("Tax rate:\t%.2f\n", taxRate);
    printf("Tax to pay:\t%d\n", taxToPay);


    return 0;
}
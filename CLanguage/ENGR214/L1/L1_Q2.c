/*/////////////////////////////////////////////
//   Title:     L1_Q2.c
//   Author:    Ryan L. 
//   Description: Calculating the annual and monthly salary
*//////////////////////////////////////////////

#include <stdio.h>

int main() {

    // needed variables (test case: 10)
    float w;
    float sal;

    // gather input from user
    printf("Enter hourly wage: ");
    scanf("%f", &w);

    //set the weekly salary
    sal = w * 40;

    //print the output to the user
    printf("Annual Salary is: %f\n", sal*50); //prints annual salary
    
    printf("Montly Salary is: %f", sal); //prints monthly salary

    return 0;
}
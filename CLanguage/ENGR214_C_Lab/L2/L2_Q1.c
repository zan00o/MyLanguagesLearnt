/*/////////////////////////////////////////////
//   Title:         L2_Q1.c
//   Author:        Ryan L.
//   Description:   C program that calculates weekly salary and assumes a limit of 40 hours per week.
*//////////////////////////////////////////////

#include <stdio.h>

int main(){

    // Declare variables (test cases: 10 42 ) (test output: 400)
    int weeklyHours, weeklyLimit, hourlyWage, overtimeHours, weeklySalary;

    // Initialize variables
    weeklyLimit = 40;

        //get input : hourlyWage weeklyHours
    printf("Enter hourly wage: ");
    scanf("%d %d", &hourlyWage, &weeklyHours);

    //calculate weekly salary

    if (weeklyHours <= weeklyLimit) {
        weeklySalary = hourlyWage * weeklyHours;
    
    } else {
        overtimeHours = weeklyHours - weeklyLimit;
        weeklySalary = (hourlyWage * weeklyLimit) + (overtimeHours * (hourlyWage * 1.5));

    }

    //print weeklySalary 
    printf("weekly salary is: %d", weeklySalary);
    

    



    return 0;
}
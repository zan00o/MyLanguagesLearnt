/*/////////////////////////////////////////////
//   Title:      Q3.c           
//   Author:     Ryan L. 
//   Description: Answer to Q3 for HW 1
*/////////////////////////////////////////////

#include <stdio.h> 

int main() { 
    // declare variables
    int days, years, weeks; 

    // prompt user for input
    printf("Enter the number of days: "); 
    scanf("%d", &days); 

    // calculate years, weeks, and days (ignoring leap years for simplicity)
    years = days  /  365; 
    weeks = ( days % 365 )  /  7; 
    days = days - (( years  *  365 ) + ( weeks  *  7 )); 

    // print results in appropriate format
    printf("Years: %d\nWeeks: %d\nDays: %d\n", years, weeks, days); 

    return 0; 
} 
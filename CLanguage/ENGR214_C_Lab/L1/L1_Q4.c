/*/////////////////////////////////////////////
//   Title:      L1_Q4.c
//   Author:     Ryan L. 
//   Description: Calculating the calories burned using age, weight, heart rate, and time
*//////////////////////////////////////////////

#include <stdio.h>

int main() {
    //declare needed variables (test case: 49 155 148 60)
    double age, weight, heart_rate, t;

    //prompt user for input of the needed variables
    printf(": ");
    scanf("%lf %lf %lf %lf", &age, &weight, &heart_rate, &t);

    //calculate the calories burned
    double caloriesBurned = (((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.499) * t) / 8.368;

    //print the calories burneD
    printf("Calories burned: %.2lf calories", caloriesBurned);
    
    return 0;
}
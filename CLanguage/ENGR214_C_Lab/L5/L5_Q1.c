/*/////////////////////////////////////////////
//   Title:         L5_Q1.c
//   Author:        Ryan L.
//   Description:   C program that determines the maximum value in a user-entered list
*//////////////////////////////////////////////
#include <stdio.h>

int main(){
    // Declare variables (test case: )
    const int NUM_ELEMENTS = 3;
    int userVals[NUM_ELEMENTS];
    int maxVal = 0;
    int i;

    // Initialize variables
        // cycles through the user-entered list and saves it to the array
    printf("Enter %d integers: ", NUM_ELEMENTS);
    for (i = 0; i < NUM_ELEMENTS; i++){
        scanf("%d", &userVals[i]);
    }

    //Work
        // cycles through the array and compares each value to the current maxVal
    for(i = 0; i < NUM_ELEMENTS; i++){
        if (userVals[i] > maxVal){
            // if the current value is greater than the current maxVal, it becomes the new maxVal
            maxVal = userVals[i];
        }
    }
    //Output
    printf("The maximum value is %d\n", maxVal);
    return 0;
}
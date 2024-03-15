/*/////////////////////////////////////////////
//   Title:         L5_Q2.c
//   Author:        Ryan L.
//   Description:   programnthat efficiently reads user-inputted values and determines the middle value
*//////////////////////////////////////////////
#include <stdio.h>
int main(){
    // Declare variables 
    const int NUM_ELEMENTS = 9;
    int userValues[NUM_ELEMENTS];
    int currValue, midIndex, i;

    // Initialize variables
        // cycles through the user-entered list and saves it to the array
    printf("Enter %d integers: ", NUM_ELEMENTS);
    scanf("%d", &currValue);
    while((currValue >= 0) && (i < NUM_ELEMENTS)){
        userValues[i] = currValue;
        i++;
        scanf("%d", &currValue);
    }
    
    //if too many numbers are entered the program will stop
    if(i>NUM_ELEMENTS){
        printf("Too many numbers");

    } else {
        //if the number of values entered is odd, the middle value is the value at index i/2
        midIndex = i/2 ;
        printf("Middle item: %d\n", userValues[midIndex]);
    }
    return 0;
}
/*/////////////////////////////////////////////
//   Title:         L6_Q3.c
//   Author:        Ryan L.
//   Description:   C program that uses the function, SwapArrayEnds() to swap 
the first and last elements of the function's array parameter.
*//////////////////////////////////////////////
#include <stdio.h>

void SwapArrayEnds(int sortArray[], int arraySize){
    int temp = sortArray[0];
    sortArray[0] = sortArray[arraySize-1];
    sortArray[arraySize-1] = temp;
    return;
}
int main(){
    // Declare & Initialize variables (test case: sortArray = {10, 20, 30, 40})
    const int arraySize = 4;
    int sortArray[4] = {10, 20, 30, 40};

    //Work
    SwapArrayEnds(sortArray, arraySize);

    printf("Swapped Array: ");
    for(int i = 0; i < arraySize; i++){
        printf("%d ", sortArray[i]);
    }
    return 0;
}
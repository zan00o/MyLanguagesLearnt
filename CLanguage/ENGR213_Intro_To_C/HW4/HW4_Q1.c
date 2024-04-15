/*/////////////////////////////////////////////
//   Title:         HW4_Q1.c
//   Author:        Ryan L.
//   Description:   program to find the sum of the series 1!/1+2!/2+3!/3+4!/4+5!/5 using the Function
*//////////////////////////////////////////////

// INCLUDES
#include <stdio.h>

// Helper function

int seriesSum(int num){
    int sum = 0;
    int fact = 1;
    for(int i = 1; i <= num; i++){
        fact = 1;
        for(int j = 1; j <= i; j++){
            fact *= j;
        }
        sum += fact/i;
    }
    return sum;
}


int main(){
    // Declare & Initialize variables (test case: 5 ) (output: 34)
    int num = 5;
    int sum;

    //Work
    sum = seriesSum(num);
    printf("Sum of the series is: %d\n", sum);

    return 0;
}
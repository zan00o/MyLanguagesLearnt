/*/////////////////////////////////////////////
//   Title:         HW4_Q2.c
//   Author:        Ryan L.
//   Description:   program to check Armstrong and perfect numbers using the function
*//////////////////////////////////////////////


// INCLUDES
#include <stdio.h>

// HELPERS
int isArmstrong(int num){
    int sum = 0;
    int temp = num;
    int digit;
    while(temp != 0){
        digit = temp % 10;
        sum += digit * digit * digit;
        temp /= 10;
    }
    if(sum == num){
        return 1;
    }
    return 0;
}

int isPerfect(int num){
    int sum = 0;
    for(int i = 1; i < num; i++){
        if(num % i == 0){
            sum += i;
        }
    }
    if(sum == num){
        return 1;
    }
    return 0;
}
    

int main(){
    // Declare variables (test case: 371) (output: is an Armstrong number, is not perfect number)
    int num;
    
    


    // Initialize variables
    num = 371;

    //Work
    
    printf("%d %s \n", num, isArmstrong(num) ? "is an Armstrong number " : "is not an Armstrong number ");
    printf("%d %s \n", num, isPerfect(num) ? "is a perfect number" : "is not a perfect number");




    return 0;
}
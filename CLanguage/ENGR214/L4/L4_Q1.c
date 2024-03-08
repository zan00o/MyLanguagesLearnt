/*/////////////////////////////////////////////
//   Title:         L4_Q1.c
//   Author:        Ryan L.
//   Description:   C program that outputs a right triangle of asterisks given the height as input.
*//////////////////////////////////////////////
#include <stdio.h>

int main(){
    // Declare variables (test case: 3 )  // * * *
    int height;                           // * *
    // Initialize variables               // * 
    printf("Enter the height of the triangle: ");
    scanf("%d", &height);

    //Work
        // itterates from 1 through the height
    for (int i = 1; i <= height; i++) {
            // itterates from the height through i 
        for(int j = height; j >= i; j--) {
                //prints the asterisk the number of times equal to i - height
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
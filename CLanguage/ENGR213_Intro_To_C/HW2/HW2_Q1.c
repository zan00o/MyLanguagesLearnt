/*/////////////////////////////////////////////
//   Title:         HW2_Q1.c
//   Author:        Ryan L.
//   Description:   C program that splits the given integer value into the smallest amount of bank notes 
(Note: possible notes include 100, 50, 20,10, 5, 2, 1) 
*//////////////////////////////////////////////
#include <stdio.h>

int main(){
    // Declare variables (test case: 375)
    int num = 0, i=0;
    int notes[7] = {100, 50, 20, 10, 5, 2, 1};

    // Initialize variables
    printf("Input the amount: ");
    scanf("%d", &num);

    //Work
    for (i = 0; i < 7; i++) {
        printf("%d Note(s) of %d.00\n", num / notes[i], notes[i]);
        num = num % notes[i];
    }
    return 0;
}
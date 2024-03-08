/*/////////////////////////////////////////////
//   Title:     L1_Q5.c           
//   Author:    Ryan L. 
//   Description: Printing the name and grade for john
*//////////////////////////////////////////////

#include <stdio.h>

int main() {
    
    //declare needed variables
    char name[] = "John";
    char grade = 'A';

    //print the name and grade with appropriate formatting
    printf("Hello %s!\nYour grade is: %c", name, grade);

    return 0;
}
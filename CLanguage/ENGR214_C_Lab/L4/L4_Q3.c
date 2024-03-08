/*/////////////////////////////////////////////
//   Title:         L4_Q3.c
//   Author:        Ryan L.
//   Description:   C program that utilizes an “enum” to define the days of the week and prints out a message
based on the day entered by the user.
*//////////////////////////////////////////////
#include <stdio.h>
enum Days {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday};

int main(){
    // Declare variables (test case: )
    enum Days day;
    // Initialize variables
    printf("Enter the day number (0 for Monday, 1 for Tuesday, ..., 6 for Sunday): ");
    scanf("%d", &day);
    //Work
        // switch statement to print a message based on the day
    switch (day) {
        case Monday :
            printf("It's a weekday, time to work.");
            break;
        case Tuesday :
            printf("It's a weekday, time to work.");
            break;
        case Wednesday :
            printf("It's a weekday, time to work.");
            break;
        case Thursday :
            printf("It's a weekday, time to work.");
            break;
        case Friday :
            printf("Its almost weekend, Lets wrap up things fast.");
            break;
        case Saturday :
            printf("It's Weekend, time to relax.");
            break;
        case Sunday :
            printf("It's Weekend, time to relax.");
            break;
        default :
            printf("Invalid day entered");
            break;
    }
    return 0;
}
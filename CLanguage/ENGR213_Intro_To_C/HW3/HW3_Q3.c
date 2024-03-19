/*/////////////////////////////////////////////
//   Title:         HW3_Q3.c
//   Author:        Ryan L.
//   Question:      Write a program to read a string from the keyboard and prints the frequency of a specific character.
*//////////////////////////////////////////////
#include <stdio.h>

int main(){
    // Declare variables (test case: This is a test string. (i))
    char str[100];
    char ch;
    int count = 0;

    // Initialize variables
    printf("Input the string: ");
    fgets(str, sizeof(str), stdin); 

    printf("Input the character to find frequency: ");
    scanf("%c", &ch);

    //Work
    for(int i = 0; str[i] != '\0'; i++){
        if (str[i] == ch){
            count++; //increments the count each time the character is found in the string
        }
    }

    //Output
    printf("The frequency of the character %c is: %d\n", ch, count);
    return 0;
}
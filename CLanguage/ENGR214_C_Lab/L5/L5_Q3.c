/*/////////////////////////////////////////////
//   Title:         L5_Q3.c
//   Author:        Ryan L.
//   Description:   C program to Capitalize the First and Last Letters of Each Word of a String.
*//////////////////////////////////////////////
#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <string.h>

int main(){
    // Declare variables (test case: )
    char str[100] = "this is a test string";
    int length;
    // Initialize variables
    length = strlen(str);

    //Work
    for (int i = 0; i < length; i++){
        if (i == 0 || i == length - 1){
            str[i] = toupper(str[i]);
        }
        if (str[i] == ' '){
            str[i-1] = toupper(str[i-1]);
            str[i+1] = toupper(str[i+1]);
        }
    }
    printf("%s", str);
    return 0;
}
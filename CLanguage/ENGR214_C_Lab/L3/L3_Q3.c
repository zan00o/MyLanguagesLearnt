/*/////////////////////////////////////////////
//   Title:         L3_Q3.c
//   Author:        Ryan L.
//   Description:   takes a phone number in the format 1-555-HOLIDAY and returns the number with the letters replaced with "?" (1-555-??????)
*//////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

int main(){
    // Declare variables (test case: 1-555-HOLIDAY)
    char phone_num[13];

    // Initialize variables
    printf(": ");
    scanf("%s", &phone_num);

    //Work
    for (int i = 0; i < 13; i++){
        
        if ((phone_num[i] >= '0' && phone_num[i] <= '9') || (phone_num[i] == '-')){
            //if i is a number or a hyphen, keep it
            phone_num[i] = phone_num[i];

        } else if (toupper(phone_num[i]) >= 'A' && toupper(phone_num[i]) <= 'Z'){
            //if i is a letter, replace it with a "?"
            phone_num[i] = '?';

        } else {
            //if i is anything else, replace it with a null character
            phone_num[i] = '\0';
        }
    }
    printf("%s", phone_num);
    return 0;
}
/*/////////////////////////////////////////////
//   Title:         L6_Q2.c
//   Author:        Ryan L.
//   Description:   program in C that uses the function, 
MakeSentenceExcited() to replace any period with an exclamation point.
*//////////////////////////////////////////////
#include <stdio.h>
#include <string.h>

void MakeSentenceExcited(char sentence[]){
    for(int i = 0; sentence[i] != '\0'; i++){
        if (sentence[i] == '.' || sentence[i] == ','){
            sentence[i] = '!';
        }
    }
    //printf("%s", sentence);
    return;
}
int main(){
    // Declare & Initialize variables (test case: I told my computer I needed a break. It replied "I am sorry, I'm not programmed for that function.")
    char userSentence[200];
    fgets(userSentence, 200, stdin);

    //Work
    MakeSentenceExcited(userSentence);
    printf("%s", userSentence);
    return 0;
}
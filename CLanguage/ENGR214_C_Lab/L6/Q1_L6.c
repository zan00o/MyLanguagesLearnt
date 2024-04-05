/*/////////////////////////////////////////////
//   Title:         L6_Q1
//   Author:        Ryan L.
//   Description:   uses a function to print shampoo instructions a specified amount and returns a void
*//////////////////////////////////////////////
#include <stdio.h>
void printShampooInstructions(int cycles){
    if (cycles <= 0){
        printf("Too Few.");
        return;
    }
    else if (cycles > 4){
        printf("Too Many.");
        return;
    }
    for(int i = 0; i < cycles; i++){
        printf("%d: Lather and rinse.\n", i+1);
    }
    printf("Done.\n");
    return;
}
int main(){
    // Declare & Initialize variables (test case: 4)
    int userCycles;
    scanf("%d", &userCycles);
    //Work
    printShampooInstructions(userCycles);
    return 0;
}
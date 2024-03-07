/*/////////////////////////////////////////////
//   Title:     L1_Q1.c            
//   Author:    Ryan L. 
//   Description: printing a pattern of specfied numbers
*//////////////////////////////////////////////

#include <stdio.h>

int main() {
    // needed variables (test case: 0 1)
    int baseInt;
    int headInt;
    
    //gather input from user
    printf("enter the numbers: ");
    scanf("%d %d", &baseInt, &headInt);
    
    //print the numbers in the required format
    printf("first problem\n");
    printf("\t%d\n",headInt);
    printf("\t%d%d\n",headInt,headInt);
    printf("%d%d%d%d%d%d%d\n",baseInt,baseInt,baseInt,baseInt,headInt,headInt,headInt);
    printf("%d%d%d%d%d%d%d%d\n",baseInt,baseInt,baseInt,baseInt,headInt,headInt,headInt,headInt);
    printf("%d%d%d%d%d%d%d\n",baseInt,baseInt,baseInt,baseInt,headInt,headInt,headInt);
    printf("\t%d%d\n",headInt,headInt);
    printf("\t%d\n",headInt);

    return 0;
}
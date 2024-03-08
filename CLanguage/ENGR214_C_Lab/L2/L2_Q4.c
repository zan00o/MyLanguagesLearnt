/*/////////////////////////////////////////////
//   Title:         L2_Q4.c
//   Author:        Ryan L.
//   Description:   C program that prints wether a given highway number is to a auxiliary or a primary highway 
// as well as prints the primary highway it serves
*//////////////////////////////////////////////

#include <stdio.h>

int main(){
    // Declare variables (test case: 90 , 290, 200)
    int highwayNum, primaryNum;

    // Initialize variables

        //get input: highwayNum
    printf(": ");
    scanf("%d",&highwayNum);

    //logic to determine if the highway is a primary or auxiliary highway

        //if not a valid highway number
    if ((highwayNum < 1) || (highwayNum > 999) || (highwayNum % 100 == 0 )) {
        printf("%d is not a valid interstate highway number", highwayNum);
    
    } else {
        primaryNum = highwayNum % 100;

            //if auxiliary highway
        if (highwayNum > 99) {
            printf("I-%d is a auxiliary highway serving I-%d",highwayNum,primaryNum);
            printf("%s",(primaryNum%2 == 0) ? ", going east/west" : ", going north/south" );

            //if primary highway
        } else {
            printf("I-%d is a primary highway",highwayNum);
            printf("%s",(highwayNum%2 == 0) ? ", going east/west" : ", going north/south" );
        }
        
    }
    
    return 0;
}
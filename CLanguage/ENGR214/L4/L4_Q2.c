/*/////////////////////////////////////////////
//   Title:         L4_Q2.c
//   Author:        Ryan L.
//   Description:   prints the sum of the series 9 + 99 + 999 + 9999 + 9[n] where n is a number input by the user.
*//////////////////////////////////////////////

#include <stdio.h>

int main(){
    // Declare variables (test case: 5 (111105))
    int n, repeatNum = 9, num = repeatNum;
    long sum = 0;
    
    // Initialize variables
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    
    //Work
        // itterates from 1 through n
    for (int i = 1; i <= n; i++) {
            // prints the number and a plus sign
        printf("%ld ", num);
        if (i < n) {
            printf("+ ");
        }
            // adds the number to the sum and multiplies the number by 10 and adds the repeat number
        sum += num;
        num = (num * 10) + repeatNum;
    }
    printf("\nThe sum of the series = %ld\n", sum);

    return 0;
}
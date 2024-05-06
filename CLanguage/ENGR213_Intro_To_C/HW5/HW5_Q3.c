/*/////////////////////////////////////////////
//   Title:         HW5_Q3.c
//   Author:        Ryan L.
//   Description:   Write a program in C to compute the sum of all elements in an array using pointers
*//////////////////////////////////////////////

#include <stdio.h>

int main(){
    // Declare variables (test case: )
    int arr[100], i, n, sum, *pt;
    
    // Initialize variables

    // Ask user for the number of elements to store in the array
    printf("input the number of elements to store in the array (max 10):");
    scanf("%d", &n);

    // Ask user for the elements to store in the array
    printf("input %d number of elements in the array :\n", n);
    for(i=0; i<n; i++)
    {
        printf("element - %d : ", i);
        scanf("%d", &arr[i]);
    }

    sum = 0;    // Initialize sum to 0

    pt = arr;   // Initialize pointer to the first element of the array

    //Work
    // Compute the sum of all elements in the array using pointers 
    for (int i = 0; i < n; i++) {
        sum = sum + *pt;
        pt++;
    }
    printf("The sum of the elements is : %d\n", sum); // Print the sum 

    return 0;
}
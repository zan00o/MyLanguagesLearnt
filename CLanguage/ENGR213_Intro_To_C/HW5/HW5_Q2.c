/*/////////////////////////////////////////////
//   Title:         HW5_Q2.c
//   Author:        Ryan L.
//   Description:   program to store n elements in an array and print the elements using pointer.
*//////////////////////////////////////////////
#include <stdio.h>

int main(){
    // Declare variables (test case: )
    int arr[100], i, n; 

    // Initialize variables
    // Ask user for the number of elements to store in the array
    printf("input the number of elements to store in the array :");
    scanf("%d", &n); 

    // Ask user for the elements to store in the array
    printf("input %d number of elements in the array :\n", n);
    for(i=0; i<n; i++) {
        printf("element - %d : ", i);
        scanf("%d", &arr[i]);
    }
   

    //Work
    // Print the elements using pointer
    printf("The elements you entered are : \n");
    for(i=0; i<n; i++){
        printf("element - %d: %d \n",i, *(arr+i));
        
    }

    return 0;
}
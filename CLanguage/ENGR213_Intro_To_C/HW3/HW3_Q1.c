/*/////////////////////////////////////////////
//   Title:         HW3_Q1.c
//   Author:        Ryan L.
//   Question:      Write a program in C to delete an element at the desired position from
*//////////////////////////////////////////////
#include <stdio.h>

int main(){

    //(test case: [1,2,3,4,5] (1 2 4 5))
    //formats the beginning of the program
    printf("Delete an element at the desired position from an array: \n");
    printf("---------------------------------------------------------\n");

    // Declare  and initialize variables
    int n, pos, i; 

    printf("Input the size of array: ");
    scanf("%d", &n); //input the size of the array
    int arr[n];

    printf("Input %d elements in the array in ascending order: \n", n);
    for (i = 0; i < n; i++){
        printf("element - %d: ", i);
        scanf("%d", &arr[i]); //input the elements of the array for the size of n
    }

    printf("Input the position where to delete: ");
    scanf("%d", &pos); //input the position to delete

    for (i = pos-1; i < n; i++){
        arr[i] = arr[i+1]; //shifts the elements to delete the desired position
    }
    //n--;

    printf("The new list is : ");
    for (i = 0; i < n; i++){
        printf(" %d ", arr[i]); //prints the new list
    }
    return 0;
}
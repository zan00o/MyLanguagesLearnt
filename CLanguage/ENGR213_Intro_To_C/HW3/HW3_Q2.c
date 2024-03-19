/*/////////////////////////////////////////////
//   Title:         HW3_Q2.c
//   Author:        Ryan L.
//   Question:      Write a program in C to print or display the lower triangular of a given matrix.
*//////////////////////////////////////////////
#include <stdio.h>

int main(){
    // Declare and Initialize variables
    int n, i;
    printf("Input the size of the square matrix: ");
    scanf("%d", &n); // input the size of the square matrix
    int arr[n][n];

    printf("Input elements in the first matrix: \n");
    for (i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            printf("element - [%d],[%d]: ", i, j);
            scanf("%d", &arr[i][j]); //input the elements of the matrix one by one
        }
    }

    // work
    printf("The matrix is: \n");
    for (i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            printf("%d ", arr[i][j]); //prints the matrix in the matrix format
        }
        printf("\n");
    }

    printf("Setting zero in the lower triangular matrix \n");
    for (i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (i > j){
                arr[i][j] = 0; //sets the lower triangular matrix to zero
                
            }
            printf("%d ", arr[i][j]); //then prints the matrix
        }
        printf("\n");
    }
    return 0;
}
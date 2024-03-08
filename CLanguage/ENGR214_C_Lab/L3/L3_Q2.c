/*/////////////////////////////////////////////
//   Title:         L3_Q2.c
//   Author:        Ryan L.
//   Description:   generates a random number between 1 and 5 and has the user guess it until they get it right
*//////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    // Declare and Initialize variables
    srand(time(NULL)); //seed random number generator
    int num = rand() % 5 + 1; //generate random number between 1 and 5
    
    int userGuess; //variable to store user's guess
    int num_attempts = 0; //variable to store number of attempts
    printf("Guess the number between 1 and 5:\n ");

    //work
    while (1){
            //get user's guess
        printf("Enter your guess: ");
        scanf("%d", &userGuess);
            //increment number of attempts
        num_attempts++;
            //check if user's guess is correct
        if (userGuess == num){
            //if correct, print number of attempts and break loop ending the game
            printf("Congratulations! You guessed the correct number in %d attempts", num_attempts);
            break;
        }
        else{
            //if incorrect, prompt user to try again
            printf("Incorrect guess. Try again!\n");
        }

    }
    return 0;
}
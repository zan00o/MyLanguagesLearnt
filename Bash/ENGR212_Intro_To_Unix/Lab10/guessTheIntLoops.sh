#!/bin/bash

#################
# Author: Ryan L.
# Date: Oct 25, 2023
# Description: Practicing conditional expressions
#################

secretInt=$((RANDOM % 100 + 0))                     #sets a random value between 0 and 100
guessedInt=-1

until [[ $guessedInt -eq $secretInt ]]              #runs until guessedInt and secretInt are equal
    do
        echo -n "enter a value between 0 and 100: " #asks the user for input
        read guessedInt                             #reads the value given

        if [[ $guessedInt -lt $secretInt ]]         #checks if guessedInt is less then secretInt
            then echo "Too Low!"                    #if so Prints "Too Low!"
            elif [[ $guessedInt -gt $secretInt ]]   #checks if guessedInt greater then secretInt
                then echo "Too High!"               #if so Prints "Too High!"
        fi
done  
echo "You Got It!"                                  #when the user guessed currectly prints "Your Got It!"

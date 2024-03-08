#! /bin/bash

#################
# Author: Ryan L.
# Date: Oct 25, 2023
# Description: Practicing conditional expressions
#################

secretInt=$((RANDOM % 100 + 0))             #sets a random value between 0 and 100
echo -n "enter a value between 0 and 100: " #asks the user for input
read guessedInt                             #reads the value given

if [[ $guessedInt -eq $secretInt ]]          #checks if guessedInt and secretInt are equal
    then echo "You Got It!"                 #if so Prints "You Got It!"
    elif [[ $guessedInt -lt $secretInt ]]     #checks if guessedInt is less then secretInt
        then echo "Too Low!"                     #if so Prints "Too Low!"
    elif [[ $guessedInt -gt $secretInt ]]     #checks if guessedInt greater then secretInt
        then echo "Too High!"               #if so Prints "Too High!"
fi



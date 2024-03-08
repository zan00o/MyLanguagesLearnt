#! /bin/bash

#################
# Author: Ryan L.
# Date: Oct 25, 2023
# Description: Practicing conditional expressions
#################

secretInt=$((RANDOM % 100 + 0))             #sets a random value between 0 and 100
echo -n "enter a value between 0 and 100: "    #asks the user for input
read guessedInt                             #reads the value given
echo "guessedInt: $guessedInt"              #prints both values to the screen
echo "secretInt: $secretInt"                #<-


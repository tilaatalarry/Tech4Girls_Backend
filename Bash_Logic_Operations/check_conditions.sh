#!/bin/bash

# Getting the numbers from the arguments
firstnum=$1
secondnum=$2

# Check if both numbers are greater than 10
if [ "$firstnum" -gt 10 ] && [ "$secondnum" -gt 10 ]; 
then
    echo "Both numbers are greater than 10."

# Check if at least one number is greater than 10
elif [ "$firstnum" -gt 10 ] || [ "$secondnum" -gt 10 ]; 
then

    echo "At least one number is greater than 10."
fi    
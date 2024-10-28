#!/bin/bash

# Get the number from the argument
number=$1

# Check if the number is even or odd
if [ $((number % 2)) -eq 0 ]; then
    echo "The number $number is even."
else
    echo "The number $number is odd."
fi

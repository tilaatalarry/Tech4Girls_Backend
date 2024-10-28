#!/bin/bash
# This script calculates the sum of numbers from 1 to n


# Assign input argument to variable
n=$1

# Calculate the sum using the formula n(n+1)/2
sum=$((n * (n + 1) / 2))

# Display the result
echo "The sum of numbers from 1 to $n is: $sum"

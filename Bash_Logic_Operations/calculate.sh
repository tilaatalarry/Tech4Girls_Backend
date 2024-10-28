#!/bin/bash

# Get the numbers from the arguments
num1=$1
num2=$2
num3=$3

# Calculate the sum of the first two numbers
sum=$((num1 + num2))

# Calculate the product of the sum with the third number
product=$((sum * num3))

echo "The sum of $num1 and $num2 is: $sum"
echo "The product of $num1 and $num2 is $product"
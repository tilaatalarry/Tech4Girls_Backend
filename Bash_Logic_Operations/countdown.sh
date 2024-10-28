#!/bin/bash

# Get the number from the argument
number=10

# Countdown loop
for ((x = number; x >= 1; x--)); do
    echo "$x"
done

echo "Countdown complete! "

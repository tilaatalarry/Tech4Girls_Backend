# #!/bin/bash 
# name="hamdallah"
# program="Tech4Girls"
# city="Accra"

# echo "Hello, I am $name, I live in city within $city, and I am a $program student"

#positional arguments in bash scripting
# $1 = script name or first argument
# $2 = second argument
# $3 = third argument

#echo "Hello $1, how are you doing?"

# echo "The first argument or the name of the script is: $0"
# echo "The second argument is: $1"
# echo "The third argument is: $2"
# echo "The fourth argument is $3"

# sum=$(($1 + $2))
# echo "The sum of $1 and $2 is $sum"

# diff=$(($1 - $2))
# echo "The difference between $1 and $2 is $diff"

# product=$(($1 * $2))
# echo "The product of $1 and $2 is $product"

# quotient=$(($1 / $2))
# echo "The quotient of $1 and $2 is $quotient"

# touch file3
# mkdir folder3
# mv "$1" "$2"
# echo "$1 has been moved into $2"

# touch file2
# mkdir folder2
# cp "$1" "$2"
# echo "$1 has been moved into $2"

#LOGICAL OR = || (only one statement needs to be true)
#LOGICAL AND = && (both statements have to be true for it to work)
#LOGICAL NOT = !

#IF STATEMENTS IN BASH
#if [condition]
# then
#    statement
#fi

# echo "How old are you?"
# read age
# if [[ "$age" -ge 18 && "$age" -le 30 ]]
# then 
#    echo "Age is valid."
# else
#    echo "Age is invalid"
# fi   

#write a script that accepts two numbers as arguments and checks if both are greater 10. 
#and if both numbers are greater than, print out "both numbers are geater than 10", if not print out 
#"one or both are not greater than 10"
# if [ "$1" -gt 10 ] && [ "$2" -gt 10 ]
# then
#    echo "Both numbers are greater than 10"
# else
#    echo "One or both are not greater than 10"
# fi

# string="Hi, ladies!"
# if [[ ! $string == "Goodbye!" ]]
# then 
#     echo "String is not equal to Goodbye"
# else
#     echo "String is equal to Goodbye"    
# fi    

#write a script that asks a user fot username, checks if the userbname is admin. 
#if the username is admin, print access granted and if its not admin, print access denied

# echo "What is your name?"
# read username
# if [[ ! $username == "Admin" ]]
# then 
# echo "Access denied"
# else
# echo "Access granted"
# fi

#WHILE LOOPS IN BASH
# while [ condition ]
# do
    # [command]
    # [command]
    # [command]
#done    

# number=1
# while [ $number -le 10 ]
# do
# echo "$number"
# number=$((number+1))
# done

# while true; do
# echo "Enter a number or type 'q' to quit"
# read number
# if [[ "$number" == 'q' ]]; then
# break
# fi
# echo "You entered $number"
# done
# echo "Exitimg the loop" 
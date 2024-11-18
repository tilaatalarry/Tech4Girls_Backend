# input build in method
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# age = age + 1
# amount = float(input("How much do you have in your account?: "))
# amount = amount * 2
# print(f'Your name, {name} and {age} has been recorded. You have {amount} in your account. ')

# prompt = "Hello! Welcome to the Rock, Paper, and Scissors game. I would like to know more information about you."
# prompt += "\n What is your name? "
# name = input(prompt)
# print(f'Welcome {name} to the game. You can start now.')

# determine if a user can go to university based on their age if the user is 18 or older, print "You are old enough 
# to enrol", else print "You will be able to enrol when you are a little older."
# age = int(input('Hello, how old are you? '))
# if age >= 18:
#     print("\nYou are old enough to enrol.")
# else:
#     print("\nYou'll be able to enroll when you are a little older.")

# write a program that asks the user what kind of rental car they would like. Then print out a message that says
# "Let me see if i can find you the {car} you would like."
# car = input("What is kind of car would you like?: ")
# print(f'Let me see if i can find you the {car} you would like.')

# write a program that asks the user how many people are in their dinner group. if the answer is more than 8,
# print a message saying "You have to wait 30 minutes for their table.", otherwise print "Your table is ready"
# Ask the user how many people are in their dinner group
# groupsize = int(input("How many people are in your dinner group? "))
# if groupsize > 8:
#     print("You have to wait 30 minutes for your table.")
# else:
#     print("Your table is ready.")

# while loop, it will continue to run so long as the condition is true
# current_number = 0
# while current_number <= 10:
#     if current_number == 5:
#         current_number += 1
#         continue
#     print(current_number)
#     current_number += 1

# write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value. 
# as they enter each topping, print a message saying "I will add {topping} to their pizza".

# Initialize a variable to store the quit value
quit_value = "quit"

# Start a loop to get pizza toppings from the user
# while True:
#     # Prompt the user for a topping
#     topping = input("Enter your preferred pizza topping (or type 'quit' to finish): ")

#     if topping == quit_value:
#         print("Order complete!")
#         break  
    
#     print(f"I will add {topping} to your pizza.")

# write a function called display_message that prints one sentence that tells everyone what you are learning,
# call the function and make sure the message displays correctly

def display_message():
    print("I am hungry")

display_message()


#write a function called favourite book that accepts one parameter called title. the finction should print out
# a message telling everyone about the book, dont forget to call the function

def favourite_book(title):
    print(f"My favourite book is {title}")

favourite_book("The Assasin's Blade")

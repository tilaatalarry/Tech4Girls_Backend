# Error and exception handling in python

# examples of a syntax error
# print("Hello Girls); missing the quotation marks at the end

# An exception is error that can disrupt the normal flow of a program. 
# Try Block: You place the code that you want to monitor for exceptions inside the try block. 
# This code is executed first. 
# Except Block: If an error occurs in the try block, the control is passed to the except block. 
# You can specify different except clauses to handle different types of exceptions.

# TYPES OF EXCEPTIONS
# 1. Zero division exception: it occurs when you try to divide a number by 0.
# example 1
# print(5/0)
# print("Hello world"); this wont run because the above command is an exception
# To fix the error, use the following block of code.
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Idiot, you can't divide a number by 0.")
# print("Hello World")        

# example 2
# print("Give me two numbers and i will divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: " )
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Idiot, you can't divide a number by 0.")    
    

# 2. Value error:  occurs when a built-in operation or function receives an argument that has the 
# right type but an inappropriate value. This often happens during type conversions or when dealing 
# with certain functions that expect a specific range or set of values.

# example 1
# print("Give me two numbers and i will divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: " )
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Idiot, you can't divide a number by 0.")  
#     except ValueError:
#         print("Numbers only, stupid.")


# 3. Except exception
# handle exceptions that may arise during the execution of the code. While you can catch specific 
# exceptions, it's also possible to catch all exceptions using a more general approach.

# example 1
# print("Give me two numbers and i will divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: " )
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Idiot, you can't divide a number by 0.")  
#     except ValueError:
#         print("Numbers only, stupid.")
#     except Exception as e:
#         print (e)
#     else:
#         print(answer)       
# 
# 4. Finally block:  used in conjunction with try and except blocks to ensure that a particular 
# section of code is executed regardless of whether an exception occurred or not.

#  example 1
# print("Give me two numbers and i will divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: " )
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Idiot, you can't divide a number by 0.")  
#     except ValueError:
#         print("Numbers only, stupid.")
#     except Exception as e:
#         print (e)
#     else:
#         print(answer)           
#     finally:
#         print("Goodbye")    


# 5. Index Error:  occurs when you try to access an index in a list (or other indexable collections, 
# such as tuples or strings) that is out of range

# example 1
# my_list = [1, 2, 3]
# try:
#     print(my_list[3])
# except IndexError:
#     print("Invalid value. Number not in range")
# else:
#     print("continue")    

# def calculate_average(numbers):
#     total = sum(numbers)
#     average = total / len(numbers)  
#     return average

# def get_numbers():
#     numbers = []
#     while True:
#         user_input = input("Enter numbers or type 'q' to quit: ")  
#         if user_input.lower() == 'q':    
#             break
#         try:
#             number = int(user_input)
#             numbers.append(number)  
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")  
#     return numbers  

# if __name__ == "__main__":
#     numbers = get_numbers()  
#     if numbers:  
#         average = calculate_average(numbers)  
#         print(f"The average is: {average}")  
#     else:
#         print("No numbers entered.")  


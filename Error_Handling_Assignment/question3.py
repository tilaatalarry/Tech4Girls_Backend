user_input = input("Enter a number: ")

try:
    converted_number = int(user_input)
    print("The number you entered is:", converted_number) 

except ValueError:
    print("The input is not a valid number. Please enter a number.")

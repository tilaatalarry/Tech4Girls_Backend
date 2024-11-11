user_input = input("Enter your age: ")
try:
    age = int(user_input)
    
    if age < 0:
        print("Age cannot be negative!")
    elif age > 120:
        print("That age is unlikely!")
    else:
        print("Your age is:", age)

except ValueError:
    print("Error: Please enter a valid numeric age.")

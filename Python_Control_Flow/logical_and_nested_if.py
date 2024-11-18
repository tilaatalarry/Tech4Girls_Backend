# Define two boolean variables
is_student = True  # Change this to test different scenarios
is_employed = False  # Change this to test different scenarios

# Check the conditions and print messages
if is_student and is_employed:
    print("You are a working student.")
elif is_student:
    print("You are a student.")
elif is_employed:
    print("You are employed but not a student.")
else:
    print("You are neither a student nor employed.")

age = int(input("Please enter your age: "))

# Check if the user is old enough to drive
if age >= 18:
    has_drivers_license = input("Do you have a driver's license? (yes/no): ")
    
    if has_drivers_license.lower() == "yes":
        print("You are allowed to drive.")
    else:
        print("You need a driver's license to drive.")
else:
    print("You are not old enough to drive.")

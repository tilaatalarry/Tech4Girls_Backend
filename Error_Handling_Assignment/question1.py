try:
    numerator = int(input("Enter the numerator: "))  
    denominator = int(input("Enter the denominator: "))  

    if denominator == 0:
        print("Denominator cannot be zero. Please enter a valid denominator.")
    else:
        result = numerator / denominator  
        print("The result is:", result)  

except ValueError:
    print("Incorrect input. Please make sure that your inputs are numbers only..")

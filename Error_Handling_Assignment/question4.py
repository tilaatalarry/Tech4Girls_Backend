items = ["apple", "banana", "cherry"]
index = int(input("Enter the index of the item you want to access: "))

try:
    print("You selected:", items[index])  
except IndexError:

    print("Index out of range. Please enter a valid index from 0 to", len(items) - 1)

except ValueError:
    print("Enter a valid integer for the index.")

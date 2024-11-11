data = {"name": "Alice", "age": 25, "country": "Wonderland"}
key = input("Enter the key you want to look up: ")

try:
    print("Value:", data[key])

except KeyError:
    print(f"The key '{key}' is not available in the dictionary.")


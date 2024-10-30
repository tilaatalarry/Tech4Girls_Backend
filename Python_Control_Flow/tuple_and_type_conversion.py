# Defining a tuple containing 5 different elements
my_tuple = (1, "apple", 3.14, "banana", True)

# Printing the first and last elements of the tuple using indexing
first_element = my_tuple[0]
last_element = my_tuple[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")

# Demonstrating the use of count() and index() methods on the tuple
apple_count = my_tuple.count("apple")
banana_index = my_tuple.index("banana")
print(f"'apple' appears {apple_count} time(s) in the tuple.")
print(f"'banana' is at index {banana_index} in the tuple.")

# Converting an integer to a float
int_value = 10
float_value = float(int_value)
print(f"Integer {int_value} converted to float: {float_value}")

# Converting a float to an integer
float_num = 3.99
int_from_float = int(float_num)
print(f"Float {float_num} converted to integer: {int_from_float}")

# Converting a string representing a number to an integer
string_num = "25"
int_from_string = int(string_num)
print(f"String '{string_num}' converted to integer: {int_from_string}")

# Joining a list of strings into a single string using join()
string_list = ["Hello", "world", "this", "is", "Python"]
joined_string = " ".join(string_list)
print(f"Joined string: '{joined_string}'")

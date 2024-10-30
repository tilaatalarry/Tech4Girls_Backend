# Defining a tuple containing 5 different elements
my_tuple = (10, "Hello", 3.14, True, "World")

first_element = my_tuple[0]
last_element = my_tuple[-1]
print("First element:", first_element)  
print("Last element:", last_element)    

count_of_10 = my_tuple.count(10)
print(count_of_10)  

index_of_Hello = my_tuple.index("Hello")
print(index_of_Hello)  

integer_value = 5
float_value = float(integer_value)
print(float_value)  

float_number = 7.89
int_value = int(float_number)
print(int_value)  

string_number = "42"
converted_int = int(string_number)
print(converted_int) 

string_list = ["Python", "is", "fun"]
joined_string = " ".join(string_list)
print(joined_string)  

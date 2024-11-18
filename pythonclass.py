#Syntax
# items = [2, 4, 6, 8, 10 ]
# for item in items:
#   if item == 8:
#        print('Skipped 8')
#         continue
#      print(item)

#for item in range(1,11):
#    print(item)


#Break statement stops a loop when a condition is met 
#Continue skips to the next value in the list   
#Enested loop(loop within a loop)

#for item in items:  #outer loop
 #   for letter in 'abc':   #inner loop
  #      print(item, letter)

#my_dict = { 'name': 'Hamdallah', 'age': 19, 'work': 'student', 'energy level': 65}
#for value in my_dict.values():
#for key in my_dict.keys():
#for key, value in my_dict.items():
#    print(key)
#    print(value)
#    print(key, value)

#Fizzbuzz challenge
# first loop through a ramgr of numbers from 1 - 50
# for i in range(1, 51):

# # if number is divisible by 3 and returns 0, print Fizz
#     if (i % 3 == 0):
#         print('Fizz')

# # if number is divisible by 5 and returns 0, print Buzz
#     elif (i % 5 == 0):
#         print('Buzz')

# # if number is divisible by 3 and 5, print FizzBuzz
#     elif (i % 3 == 0 and i % 5 == 0):
#         print('FizzBuzz')

# # else, print the number
#     else:
#         print(i)

# create a dictionary called students with keys, name, age and city and corresponding values. Use a for loop
# to print each key value in the format key:value

# students = {
#     "name": "Hamdallah",
#     "age": 19,
#     "city": "Accra"
# }
# for key, value in students.items():
#     print(f"{key}: {value}")

#                   OR

# student = { 'name': 'Hamdallah', 'age': 19, 'city': 'Accra'}   
# for key, value in student.items():
#     print(f"{key}: {value}")

# create a list called grades containing (85 72 90 68 80), use a for loop to print out only the grades 
# that are about 80. calculate and print out the average of all the grades. 

# grades = [85, 72, 90, 68, 80]

# print("Grades above 80:")
# for grade in grades:
#     if grade > 80:
#         print(grade)

# average = sum(grades) / len(grades)

# print("Average of all grades:", average)

# create a list of tuples called products containing product names and prices: 
# products = [("apple", 1.29), ("banana", 0.59), ("orange", 0.79)].
# use a for loop to unpack each tuple and print "Product: [name] - Price [price]".

# products = [("apple", 1.29), ("banana", 0.59), ("orange", 0.79)]

# for product, price in products:
#     print(f"Product: {product} - Price: {price}")

# #                                    OR

# products = [("apple", 1.29), ("banana", 0.59), ("orange", 0.79)]

# for product in products:
#     print("Product:", product[0], "- Price:", product[1])

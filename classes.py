# OOP: Object Oriented Programming is the most effective approach to writing software. You create or write 
# classes that represent real world things and situations and then create objects that are based on the objects.
# Classes define the behaviour of the whole categoryb of objects.  
# Objects are derived from classes.
# The process of making an object from a class is called instantiation.
# We use less code in OOP.

# class Human:
#     #defining a model for humans
#     def __init__(self, name, age, hobby): # runs automatically whenever an instance is created based on the class.
#         self.name = name
#         self.age = age
#         self.hobby = hobby

#     def eat(self):
#         #makes a human eat
#         return f'{self.name} is eating'   
    
#     def drink(self):
#         #makes a human drink water
#         return f'{self.name} is drinking coca-cola'
    
#     def school(self):
#         #makes a human go to school
#         return f'{self.name} is going to school'
     

# human1 = Human("Precious", 21, "asking questions")
# human2 = Human("Priscilla", 24, "snapchatting")

# print(human1.eat())
# print(human2.drink())
# print(human1.school())

# print(human1.name)
# print(human2.name)
# print(human1.age)
# print(human2.age)
# print(human1.hobby)
# print(human2.hobby)

# human1.name = "Hamdallah"
# human1.age = 19
# human1.hobby = "Eating"

# human2.name = "Sarah"
# human2.age = 20
# human2.hobby = "I don't know"

# print(human1.name)
# print(human1.age)

# QUESTION 1
# Make a class called resturant. the init method for resturant should store 2 attributes: resturant 
# name and cuisine type. Make a method called describe resturant that print 2 pieces of infomation 
# and another method called open resturant that prints a message indicationg the resturant is opened
# Make 2 instances from your resturant class. 
#Print 2 attributes individually and call both methods

# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"Restaurant Name: {self.name}")
#         print(f"Cuisine Type: {self.cuisine_type}")

#     def open_restaurant(self):
#         print(f"{self.name} is now open!")

# restaurant1 = Restaurant("Pasta Haven", "Italian")
# restaurant2 = Restaurant("Sushi Dushi", "Japanese")

# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()

# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()

# QUESTION 2
# make a class called user, create 2 attribites called first name and last name and then create several other 
# attributes that are typically stored in a user profile. make a method called describe_user that prints a 
# summary of the user's onfo. make another method called greet_user that makes a personalised greeting for 
# the user. create several instances representing different several users and call both methods for each user.

# class User:
#     def __init__(self, first_name, last_name, age, phone_number, email, country):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.phone_number = phone_number 
#         self.email = email
#         self.country =  country

#     def describe_user(self):
#         print(f"Your first name: {self.first_name}")
#         print(f"Your last name: {self.last_name}")
#         print(f"Your age: {self.age}")
#         print(f"Your phone number: {self.phone_number}")    
#         print(f"Your email address: {self.email}")
#         print(f"Your country: {self.country}") 

#     def greet_user(self):
#         print(f"Welcome back, {self.first_name}! How may i assist you today?")     

# user1 = User("Hamdallah", "Abdallah Waniyaki", 19, +233575274945, "hawaniyaki@gmail.com", "Ghana")
# user2 = User("Lily", "Cross", 24, +13456782109, "lils.cross@yahoo.com", "Canada")
# user3 = User("Chris", "Brown", 35, +13456789054, "chrisbrown@icloud.com", "USA")         

# user1.describe_user()
# user1.greet_user()

# user2.describe_user()
# user2.greet_user()

# user3.describe_user()
# user3.greet_user()


''''----------------   INHERITANCE   ----------------'''

'''This is when a class inherits from another class.
We do this when we want to create a class that is similar to an already existing class
The already existing class is called the parent class and the one inheriting is the child class
The child class can access any or all of the attributes and methods of the child class'''




class Employee:
    raise_amount = 0.05 # this is the raise amount by which the pay is increased
    num_of_employees = 0

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = f'{firstname}.{lastname}@gmail.com'.lower()

        # In this main method we can increase the number of employees after every instance of the class
        Employee.num_of_employees += 1

    def show_full_name(self):
        return f'{self.firstname} {self.lastname}'
    
    def raise_pay(self):
        new_pay = self.pay + (self.pay * self.raise_amount) # or Employee.raise_amount
        return new_pay
    

    ''''----------------   CLASS METHODS   ----------------'''

    '''They are different from instance methods. Instance methods take the self parameter.
    Class methods are associated with the class itself instead of the instances
    These methods are for the class
    to create a class method we make use of decorators
    They are like functions that take another function as an argument and returns a modified version of that function
    Decorators look like this: @classmethod
    They take "cls" as their first argument instead of self'''

    @classmethod
    def set_pay_percent(cls, amount):
        cls.raise_amount = amount
        print(f'Pay percentage has been raised to {amount}')



# This class inherits from the employee class

class Software_Engineer(Employee):
    def _init_(self, firstname, lastname, pay, prog_lang):
        super()._init_(firstname, lastname, pay)
        self.prog_lang = prog_lang

class Project_Manager(Employee):
    def _init_(self, firstname, lastname, pay, department):
        super()._init_(firstname, lastname, pay)
        self.department = department
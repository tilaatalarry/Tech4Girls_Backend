class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

my_car1 = Car("Toyota", "Camry", 2020)
my_car1.display_info()

my_car2 = Car("Mercedes-Benz", "GLE", 2024)
my_car2.display_info()

my_car3 = Car("BMW", "M5", 2023)
my_car3.display_info()
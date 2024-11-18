from classes import Employee

class Software_Engineer(Employee):
    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang

engineer1 = Software_Engineer("Talatu", "Nyande", 2000, "python")
engineer2 = Software_Engineer("Nana", "Afua", 4000, "javascript")
engineer3 = Software_Engineer("Rahma", "Zakaria", 3500, "c++")

class Manager(Employee):
    #modelling a manager
    def __init__(self, firstname, lastname, pay, employees=None):
        super().__init__(firstname, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        #add an employee to manager's list of employees
        if emp not in self.employees:
            self.employees.append(emp)
        return f"Employee {emp.show_full_name()} has been added to manager's employees"

    def show_all_employees(self):
        #prints out all employees for the manager
        for emp in self.employees:
            print(f"Manager is managing these employees\n {emp.show_full_name()}")


new_manager = Manager("Hamdallah", "Abdallah Waniyaki", 40000, [engineer1])
print(new_manager.show_full_name())
print(new_manager.add_employee(engineer2))
print(new_manager.add_employee(engineer3))
new_manager.show_all_employees()
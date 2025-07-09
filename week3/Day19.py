#Day19:Inheritance
#Example 1
# Base class
class Employee:      #Parent Class
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}")

# Subclass
class Manager(Employee):    #Child Class
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)    #Used to access the method of parent class
        self.department = department

    def show_department(self):
        print(f"Department: {self.department}")

manager1 = Manager("Alice", "M123", "HR")  #Creating Object

manager1.display_info()     # From Employee class  #Method Call
manager1.show_department()  # From Manager class


#Example 2
class Appliance:
   def __init__(self,brand,power):
        self.brand = brand
        self.power = power
   def show_specification(self):
        print(f"Brand: {self.brand}")
        print(f"Power: {self.power}")

class WashingMachine(Appliance):
    def __init__(self,brand,power,capacity):
        super().__init__(brand,power)
        self.capacity = capacity

    def show_capacity(self):
        print(f"Capacity:{self.capacity}")
WM1=WashingMachine("LG",220,10)
WM1.show_capacity()
WM1.show_specification()


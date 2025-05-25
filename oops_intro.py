# 05_oops_intro.py
"""
Introduction to Object-Oriented Programming (OOP) Concepts in Python
--------------------------------------------------------------------

Key OOP Concepts:
1. Class: Blueprint for creating objects (a template)
2. Object: An instance of a class
3. Inheritance: Mechanism to derive a new class from an existing class
4. Encapsulation: Hiding internal details and exposing only what is necessary
5. Abstraction: Hiding complex implementation and showing only essential features
"""

# 1. Class and Object
class Employee:
    company_name = 'TATA CONSULTANCY SERVICES'  # Class variable

    def __init__(self, name, salary):
        self.name = name        # Instance variable
        self.salary = salary    # Instance variable

    def show(self):
        print(f'Employee Name: {self.name}, Salary: {self.salary}, Company: {self.company_name}')

# Creating objects (instances)
emp1 = Employee("Harry", 12000)
emp2 = Employee("Emma", 10000)

emp1.show()
emp2.show()

print("\n--- Inheritance Example ---")
# 2. Inheritance - Child class inherits from Parent class
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call parent constructor
        self.department = department

    def show_manager(self):
        print(f'Manager Name: {self.name}, Department: {self.department}, Salary: {self.salary}')

mgr = Manager("Sophia", 20000, "IT")
mgr.show()
mgr.show_manager()

print("\n--- Encapsulation Example ---")
# 3. Encapsulation - Private variables
class EncapsulatedEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # Private variable

    def show(self):
        print(f'Name: {self.name}, Salary: {self.__salary}')

    def get_salary(self):
        return self.__salary

emp_encap = EncapsulatedEmployee("Jessa", 40000)
emp_encap.show()
# print(emp_encap.__salary)  # This will cause an error due to private variable
print("Access salary via method:", emp_encap.get_salary())

print("\n--- Abstraction Example ---")
# 4. Abstraction - Using abstract classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(f"Circle area: {c.area()}")

# You cannot instantiate abstract class Shape
# shape = Shape()  # This will raise an error

"""
Summary:
- Class: Template to create objects
- Object: Instance of a class
- Inheritance: Child class inherits attributes/methods from parent class
- Encapsulation: Hide data to protect it
- Abstraction: Show essential features, hide complexity
"""

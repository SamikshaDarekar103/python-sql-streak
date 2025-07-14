#Day20:Covering concepts class,functions,Conditional statement and Operators
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Marks: {self.marks}")

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

name = input("Enter student name: ")
marks = float(input("Enter marks (out of 100): "))
student1 = Student(name, marks)
student1.display()
print("Grade:", student1.grade())

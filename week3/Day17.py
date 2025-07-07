#Class:A class is like a blueprint for creating objects(As a template)

class Student:
    def __init__(self, name, grade):  #Constructer Method (Runs when new object is created)
        self.name = name      # attribute
        self.grade = grade    # attribute

    # Method
    def introduce(self):
        print(f"My name is {self.name} and I'm in grade {self.grade}.")

student1 = Student("Alice", 10) #Object
student2 = Student("Bob", 12)

student1.introduce() #Method Call
student2.introduce()

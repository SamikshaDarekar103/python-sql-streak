#Day18:Create a Class Student that takes name and marks of 3 subjects as a arguments in constructor.
#Then create a method which prints the average
class Student:
    college="Sinhgad College Of Engineering"  #This is a class level attribute
    def __init__(self,name,marks):    #Constructor
        self.name=name
        self.marks=marks
    @staticmethod      #Decorator
    def welcome( ):    #This is a static method which work at Class level
        print("Welcome To Student Class")

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",self.name,"Your average is" ,sum/3)


s1=Student("Samiksha",[20,30,40])
s1.welcome()
print("You are from",Student.college)
s1.get_avg()



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

#Problem2: Create a Class Account with two attributes account number and balance.
#Create a methods for credit,debit and printing the balance
class Account:
    def __init__(self,acc,balance):
        self.acc=acc
        self.balance=balance

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"is Credited")
        print("Your Total Balance is :",self.get_balance())
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"is Debited")
        print("Your Total Balance is :", self.get_balance())
    def get_balance(self):
        return self.balance

acc1=Account(907865,40000)
print(acc1.acc,acc1.balance)
acc1.credit(10000)
acc1.debit(10000)



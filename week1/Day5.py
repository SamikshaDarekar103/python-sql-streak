#Day5:Types of Operators
#Python Supports Various types of operators 1]Arithmatic 2]Assignment 3]Comparison 4]Logical 5]Identity 6]Membership

#1]Arithmatic Operators[+,-,*,/,%,**]
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
print("Addition=",num1+num2)#Addition
print("Subtraction=",num1-num2)#Subtraction
print("Multiplication=",num1*num2)#Multiplication
print("Division=",num1/num2)#Division
print("Modulo=",num1%num2)#Modulus(Remainder)
print("Exponentiation=",num1**num2)#Exponentiation

#2]Assignment Operators[=,+=,-=,*=,/=]
num=10 #Assign the value
num+=5 #Add and assign
print(num) #Output:15
num-=5 #Subtract and assign
print(num) #Output:10
num*=5 #Multiply and assign
print(num) #Output:50
num/=5 #Divvide and assign
print(num) #10

#3]Comparison Operators [==,<=,>=,!=,>,<]
print("Equal to=",5==5) #equal to (Output:True)
print("Not equal to=",10!=20) #not equal to (Output:True)
print("Greater Than=",20>15) #Greater Than (Output:True)
print("Less Than=",20<15) #less than (Output:False)
print("Greater Than and Equal to=",20>=15) #greater than equal to (Output:True)
print("Less Than and Equal to=",20<=15) #less than equal to (Output:False)

#4]Logical Operators [and,or,not]
x=20
print("AND Operation=",x>10 and x<30) #If both the conditions are True Then it will return 'True' (Output:True)
print("OR Operation=",x<10 or x<30) #If any one condition is true then it will return 'True'     (Output:True)
print("NOT Operation=",not x>10) #It Inverts the result that is True become false and vice versa   (Output:False)

#5]Identity Operators [is,is not] (Used to check if two objects refer to the same memory location)
print("Identity Operators")
x=10
y=10
print(x is y) #Returns True (The Location ID of x and Y are same)
print(id(x))
print(id(y))
a=10
b=20
print(a is b) #Returns False
print(a is not b) #Returns True

#6]Membership Operator [in,not in] (This operators are used to test whether a specific value is present within a sequence such as string,list,tuple,set)
print("Membership Operators")
str1='apple'
print('a' in str1) #it checks if character a is present in str1 if yes then it returns True (Output:True)
print('b' in str1) #(Output:False)
print('b' not in str1) #(Output:True)

customers=['samiksha','Richa','Priti']
name=input('Enter your name:')
if(name in customers):
    print("Welcome")
else:
    print("Access Denied")





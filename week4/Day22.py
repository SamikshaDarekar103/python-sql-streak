#Day21:Exception handling
a=10
b=0
#print(a/b)   #This will give error(Complex statement) because we cannot divide a number by 0
#To avoid such errors we use exception handling
try:   #We write a statement which may give a error
    print(a/b)
except Exception as e:  #In this block we perform the operations which will be perform if the error occur(Execute only when you have error)
    print("Number cannot divided by zero",e)
finally:  #This will execute if we get error as well as if we dont get error
    print("Done")

#Example 1:List Index Finder with Exception Handling
l1=["Hello",32,"Word",43,21,1]

try:
    target = int(input("Enter the Index"))
    print(l1[target])
except ValueError as e:
    print("Enter Integer Value",e)
except IndexError as e:
    print(e)


#Example2:Division Calculator with Exception Handling
num1=int(input("Enter the First Number"))
try:
    num2=int(input("Enter the Second Number"))
    print(num1/num2)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("Something went wrong",e)

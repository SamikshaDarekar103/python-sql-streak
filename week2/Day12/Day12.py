#Day12:Modules=A module is a file containing a set of codes or a set of functions which can be included to an application
#We can create module using ".py" extension
#We can import module using "import module_name" in program
#The reusability of code increases
import Calculator   #Imported the Module Calculator
#from Calculator import add, sub,mul,div (we can also do like this)

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
print("Addition:",Calculator.add(num1, num2))
print("Subtraction:",Calculator.sub(num1, num2))
print("Multiplication:",Calculator.mul(num1, num2))
print("Division:",Calculator.div(num1, num2))



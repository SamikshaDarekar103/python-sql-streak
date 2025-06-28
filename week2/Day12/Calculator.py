#This is a module which perform basic maths operations

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 == 0:
        print("Division by zero")
    else:
        return num1 / num2

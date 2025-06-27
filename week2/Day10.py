#Day10:Write a Function to find a factorial
#Factorial is n!
#eg 5!=1*2*3*4*5=120
def cal_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial *= i
    print(factorial)

cal_factorial(5)


#Write a function to convert USD value into INR value
def converter(USD_Value):
    INR_Value=USD_Value*83
    print("USD=",USD_Value,"INR=",INR_Value)
converter(50)
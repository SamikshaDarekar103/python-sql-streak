#Day16:Write a Function for Fibonacci series 
def fibonacci(n):   #Function Definition
    n1, n2 = 0, 1
    count = 0
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

num_terms = int(input("How many terms? "))
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci(num_terms)

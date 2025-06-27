#Day11:Recursion:When a Function call itself recursively
#Recursion is similar to loops
def show(n):
    if n==0 :         #This is Base Case:This ends the recursion and Prevents infinite loops.
        return
    print(n)
    show(n-1)         #This is Recursive Case:The function calls itself

show(5) #it will print 5,4,3,2,1

#Q1:Write a Recursive Function To Find Factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

#Q2:Write a recursion function to calculate the sum of n natural numbers
def add(n):
    if n==0:
        return 0
    else:
        return n+add(n-1)
print(add(5))

#Q3:Write a Recursive function to print the all elements in list
def print_list(list,index):
    if index==len(list):
        return
    print(list[index])
    print_list(list,index+1)
l1=[1,2,3,4,5]
print_list(l1,0)



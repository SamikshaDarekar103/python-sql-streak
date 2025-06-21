#Day9:Functions
#function is a block of code which perform specific and repeated Tasks
#The Redundancy of code will decrease because of Functions

#Function Definition
def addition():   #Function without parameters
    a=int(input("enter a"))
    b=int(input("enter b"))
    sum=a+b
    return sum  #Used to return the output
add=addition()  #Function call
print(add)


#Function definition
def addition2(num1,num2):   #Function With Parameters (num1 and num2 are parameters)
    sum=num1+num2
    print(sum)
addition2(12,45)    #Function Call (12 and 45 are arguments)(here num1=12 and num2=45)
addition2(30,56)
addition2(90,23)


#Write a Function To return the average of 3 numbers
def average(n1,n2,n3):
    sum=n1+n2+n3
    avg=sum/3
    print(avg)
average(10,20,30)
average(1,2,3)


#write a function to print the length of list and to print the elements of list on separate line
cities=["Pune","Mumbai","Chennai","Punjab"]
marks=[45,21,56,78,90]
#Function Definition
def fun_lists(l1):  #Parameter in l1
    length=len(l1)
    for i in l1:
        print(i,end="\n") #To print it on separate line
    print("Length Of list is= ",length)
fun_lists(cities)  #Function call with argument list cities
fun_lists(marks)   #Function call with argument list marks


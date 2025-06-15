#Day 3 - Control Flow(Conditional Statements and Loops): Use if, elif, else,for,while

#These statements are used to execute different blocks of code based on whether a condition is True or False
#Following is a example of Traffic Signal
light=input("Enter the Color of light")
if light=="red":
    print("Stop")
elif light=="yellow":
    print("Be Ready")
elif light=="green":
    print("goo")
else:
    print("Light is broken")

###Looping statements are used to repeatedly execute a block of code as long as a specified condition is true.

#Syntax of for loop is= for variable in range(start,end,Increment/Decrement) although start and increment is optional
for i in range(0,101,10):  #This is for Loop(The Index of loop is start from '0')
    print(i)
for i in [23,45,12,34]:
    print(i)
for i in range(90,80,-1):
    print(i)

#While Loop
i=1
while i<10:   #Condition
    print(i)  #Output
    i=i+1     #Increment/Decrement

j=10
while j>=0:
    print(j)
    j=j-1

#Break and Continue Statements In python
#Break exits the loop immediately when a certain condition is met.
nums=[1,2,3,6,-7,8,9]
for i in nums:
    if i<0:
        break
    print(i) #Output of this will be upto 6

#Continue skips the current value and go to the next value
nums=[11,12,234,6,-27,88,90]
for i in nums:
    if i<0:
        continue
    print(i) #continue statement skip the value which doesn't satisfy the value and print next value the output will be every value except -27

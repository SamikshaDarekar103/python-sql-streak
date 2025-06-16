#Day4: Creating string, indexing, slicing, string methods, and f-string
#A string is a sequence of characters enclosed in quotes.
#Creating String
first='Samiksha'
last='Darekar'
print(first,last)

#Indexing:We can access characters in a string using index numbers(index start from 0)
print(first[0]) #The Output will be s
print(first[-1])#The output will be a(We can traverse string backward)

#Slicing:we can extract a part of a string using slicing
#Stntax:string[start:end]
code="Programming"
print(code[0:4])#The Output will be Prog (it exclude the 4th Character)
print(code[:6])#The Output will be Progra
print(code[7:])#The Output will be ming
print(code[:-4])#the output will be Program
print(code[0:-4])#the output will be Program
print(code[-4:-6])#It will give empty string because slicing goes left to right

#Concatination: Use '+' operator to concat that means join the string
full_name=first+' '+last
print(full_name) #Print Samiksha Darekar

#various Methods Of strings

text = "  python programming  "
#1.strip:Removes the spaces
print(text.strip())
#2.length:Gives the length of string
print(len(text))#Output will be 22
#3.lower:convert full string into lowercase
print(text.lower())
#4.upper:convert full string into uppercase
print(text.upper())
#5.replace: used to replace the word into string(syntax:string.replace(old,new))
print(text.replace("python","java"))
#6.split:split the string by spaces into list
print(text.split())

#f-string(formatted sting)
#f-Strings used to insert variables directly inside strings.(it uses {} to insert variable)
print(f"My First Name is {first} and Last Name is {last}")#first way
print("My First Name is {} and Last Name is {} ".format(first,last))#second way


print(f"I am {full_name.upper()} and I am larning {text.strip().upper()}")



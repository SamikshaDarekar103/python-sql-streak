#Day8:List,Tuple,Set,Dictionary in Python
#1]Lists:list is Ordered,Mutable and allow Duplicates
marks=[40,60,35,69] #Creating list
marks.append(90) # adding element at the end of the list
marks.insert(2,80) # add element at specific index
print(marks)
marks.remove(69) #removes the specified element
marks.pop(0) #remove the element from specified location
print(marks)
print(marks[2]) #Access the element
print(sorted(marks)) #sort elements in ascending order
marks.clear() #It removes all the elements from list


#2]Tuples: Tuples are Ordered,Immutable and Allow Duplicates(Tuple does not support Modification)
num=(32,45,55,90,45,55) #creating tuple
print(num)
print(num.count(55)) #Number of time the specified element occur
print(num.index(55)) #Returns the index of first x


#3]Set:Sets are Unordered(it does not maintain the order),Mutable and Does not allow duplicates
color={'red','green','blue','yellow'}
color.add('pink')
color.remove('pink')
print(color)

s1={12,33,45,65,55}
s2={21,33,65,89,90}
print(s1.union(s2)) #Returns union of sets
print(s1.intersection(s2)) #Returns common elements
print(s1.difference(s2)) #Returns elements in s1 not in s2
print(s2.difference(s1)) #Returns elements in s2 not in s1
print(s1.issubset(s2)) #Checks if set s1 is subset of s2



#4]Dictionary:Ordered,Mutable,does not allow duplicates,represent in Key:Value Pair(The Key should be unique)
student={"name":"Samiksha","age":20,"Grade":"A"}
student["College"]="SCOE" #Add the key:value pair in dictionary
print(student.get("College")) #Returns value for specify key (retriv the value using key)
print(student.keys()) #Returns all keys
print(student.values()) #Returns all values
print(student.items()) #Returns all key-value pairs
student.update({"age":21}) #Updates the value
student.update({"Placement":"Yes"}) # Also used to add the key:value pair in dictionary
print(student)
print(student.pop("Grade")) #Removes and returns value for Given key
print(student.popitem()) #Removes and returns last inserted pair i.e "Placement":"Yes"
print(student)








#A tuple is a data type used to store multiple values in a single variable.
#It is similar to a list, but the main difference is that tuples are immutable (cannot be changed).
#followed by () parenthesis
#Ordered (items have fixed positions)Practice problems with answers
#Immutable (cannot modify after creation)
#Allows duplicate values
#Can store different data types




t1 = ()  # Empty tuple
t2 = (1,2,3)# Tuple with elements
t3 = 10,20,30 # Without parentheses (tuple packing)
t4 = (1,"Pandu, 3.5")# Mixed data types



tuple = (3,4,6,7,4) # Declaration of the tuple

for i in tuple :
    print(i) # prints the tuple one by one



print("First element in the tuple is : ",tuple[0])              # Accesing the first element , we have to use [] while accesing 
print("Last element in the tuple is :",tuple[-1])   # accesing the last element using slicing index

length = len(tuple) #calculates the length of the tuple
print("Length of the tuple is : ",length) # prints length

el = int(input("Enter any number to find in the tuple : ")) # takes the input from user

if(el in tuple) :
    print("Element found") # prints the index of the element if the element is found
else :
    print("Element not found") # prints if the if condition is false



occur = int (input("Enter any number to find the occcurance : ")) # Takes input of the element

if occur in tuple :
    print("Occurence of the element in the tuple is : ",tuple.count(occur), ", at = " , tuple.index(occur)) # prints the occurance of the element 
                                                                                                          #if the occur element is in the tuple
                                                                                                          #and prints the first occurence index of that element 
else: 
    print("Enter a valid number") # Prints if the occur element is not in the tuple 

big = max(tuple) # Finds the max value and stores in the big var
print("Largest number in the tuple is : ", big) # prints the max value in the tuple

small = min(tuple) #Finds the min value and stores in the small var
print("Smallest number in the tuple is : ",small) # prints the min value in the tuple


lis = list(tuple) #converts the tuple into the list form

print(  "Type of the lis is :",type(lis), "Elements : ",lis) # prints the type of the lis and tuple in the list form

t11 = (1,2,3)
t22 = (4,5,6)

print("Concatination of the two tuples is : ",t11 + t22) # coconcatinates the two tuples t11 and t22 into a single tuple and prints the concatnated tuple

print("Slicing the tuple from the index 2-5 is : ", tuple[2:5]) # prints the tuple from the index 2 to 5

s = set(tuple)  # coverts tuple to set to remove duplicates
print("Tuple after removing duplicates : ", s) # prints the tuple without duplicates

data = ("Pandu" , 18 , "Male") # packing the data into a tuple

name,age,gender = data # unpacking the data and assigning to variables based on the index

print("Name : " , name)#prints the index [0]
print("Age : " , age)  #prints the index [1]
print("Gender : ", gender)#prints the index [2]


a = 10
b = 20

print("a = ",a , "b = ",b) #prints the values of a and b before swaping


a,b = b,a #swapping executes

print("a = ",a , "b = ",b) #prints the values of a and b after swaping


add = (3,453,34,56,32,54) # tuple declration
 
print("sum of all digits in the tuple is : ",sum(add)) #adds all the elements in the list and prints the total sum

reverse = add[::-1] # reverses the tuple 

print("tuple in the reverse order is  :",reverse) #prints the tuple in reverse order

t = (1, (2, 3), 4) #nested tuple 

print(t[1])      # (2, 3) accesing main tuple elements
print(t[1][0])   # 2   accesing the nested tuple elements

x= (1, 2, 3)
y = (2, 3, 4)

common = tuple(set(x) & set(y)) # finds all the common elements and stores into common var

print(common)# prints all common elements 


tu= (1, "hello", 2.5, 3)

for i in tu :
    if type(i) == int: # finds all the integers
        print(i)  # prints only integers from the tuple
#Dictionary is a build in data type in python that asscessed through {Key:value,} pairs.
#Stores data as key : value
#Keys must be unique   **********
#Keys are usually strings, numbers, or tuples
#Values can be any data type
#Dictionaries are mutable (can change) *****


#____________________________********BASIC SYNTAX***********_____________________________________

my_data = {       # Declaration of a dictionary
    "name": "Dileep Prasad",  #Key : value,
    "age": 18,
    "course": "B-Tech"
}

print("My name is : ",my_data["name"])   # Output: Dileep , accessing value through key
print("I'm" ,my_data["age"] , "years old" )   # Output: 18 , accessing value through key
print("Im studing : ",my_data["course"])   # Output: B-tech , accessing value through key


my_data["City"] = "Rajkot" # adding new key : value pair
my_data["College"] = "Marwadi university"  

print(my_data)  # prints the new dictionary with updation

my_data.pop("City")  #Removes city key along with its value  here we use (parenthesis)

print(my_data)# prints the dictionary by removing city key:value pair

#*************************** USE OF LOOPS IN DICTIONARY ***********************************


for key,values in my_data.items() : # accessing key value pairs using loops
    print(key , values) # prints all key values pairs

print (my_data.keys())    # Returns all keys
print (my_data.values())  # Returns all values
print (my_data.items())  # Returns key-value pairs


#***************************** REAL WORLD EXAMPLE ********************************************



student = {
    "name": "Dileep",
    "marks": 94,
    "grade": "o"
}

# Access data
print(student["grade"])

# Update marks
student["marks"] = 98

# Add new field
student["city"] = "Rajkot"

print(student) # prints updated data

print(len(student)) # prints the number of key:values pairs 

print("name" in student) # Checks if the key exists , True is exists and False if does'nt


sq = {} # Empty dictionary

for i in range(1, 6): #(start,stop)
    sq[i] = i * i   # stores the square of the key as their in sq dictionay

print(sq) # prints the dictionary as key : square of the key as values

dict1 = {1: "a", 2: "b"}
dict2 = {3: "c", 4: "d"}

dict1.update(dict2) # using update function we merge dict2 into dict1
print(dict1)# prints the dict1 as merged dictionary

grade_marks = {"A": 80, "B": 95, "C": 70}
print(max(grade_marks.values()))  # finds the max value in dict and prints it


marks = {"A": 40, "B": 60, "C": 90}

for k, v in marks.items(): 
    if v > 50: # checks the values in the dictionary  if they are above 50 or not
        print(k) # prints the key , if the values  are more than 50



#********************NESTED DICTIONARY***********************

students = {
    "s1": {"name": "A", "marks": 80, "city": "Delhi"},
    "s2": {"name": "B", "marks": 70, "city": "Mumbai"},
    "s3": {"name": "C", "marks": 90, "city": "Pune"}
}
print(students) #Prints the nested dictionary

#****************Sort by Keys************************

d1 = {3: "c", 1: "a", 2: "b"}

for k in sorted(d1): # sorts the key:value pairs in ascending order using keys
    print(k, d1[k])


#****************Sort by Values************************

d2 = {"A": 80, "B": 60, "C": 90}

sorted_d2 = dict(sorted(d2.items(), key=lambda x: x[1]))
print(sorted_d2)



#****************Invert Dictionary************************

d = {1: "a", 2: "b"}

inv = {}
for k, v in d.items():
    inv[v] = k   # Assigns the dictionary d values as keys of the inv dictionary

print(inv)



#****************Removes Duplicate values************************


old_d = {"A": 80, "B": 80, "C": 70}

new_d = {}
for k, v in old_d.items():
    if v not in new_d.values():
        new_d[k] = v

print(new_d)
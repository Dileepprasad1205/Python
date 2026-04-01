#File I/O (Input/Output) in Python is used to read data from files and write data to files. 
#It allows your programs to store data permanently instead of losing it when the program ends.

#***************************************COMMON MODS*****************************************


#| Mode  | Meaning                   |
#| ----- | ------------------------- |
#| `"r"` | Read (default)            |
#| `"w"` | Write (overwrites file)   | also creates file if it doesn't exists
#| `"a"` | Append (adds data at end) | also creates file if it doesn't exists
#| `"x"` | Create new file           |
#| `"b"` | Binary mode               |
#| `"t"` | Text mode (default)       |



#1. Opening a File (syntax)

file = open("filename.txt", "mode")



#2. Reading a File

file = open("data.txt", "r") #opens a file in read mode
content = file.read()  #reads the file
print(content)  #prints the data int the file
file.close()  # closes the file

#3.   readline() : Reads only one line at a time

file = open("data.txt", "r")
print(file.readline()) # reads the first line in the file
file.close()


#4. readlines() : Reads all lines as a list

file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()

#5. Writing to a File

file = open("data.txt", "w")  #opens a file in write mode
file.write("Hello Python")  # writes the file  after truncating it , This will overwrite existing content.
file.close()


#6.  append mode , appends at the end of the file  without truncating or overwriting it

file = open("data.txt", "a")
file.write("\nNew Line Added")
file.close()

#*********************************Recommended syntax***************************
# using (with) statement because ,  This automatically closes the file

with open("data.txt", "r") as file: # for opening in read mode
    content = file.read()
    print(content)

with open("data.txt", "w") as file: # for opening in write mode
    file.write("Hello World")



#7. Working with File Paths 
 
with open("C:/Users/YourName/Desktop/file.txt", "r") as file: # if the file doesn't exist in the same folder we need to give the complete path
    print(file.read())



#*********************************Important Points***************************

#Always close files (file.close()) or use with
# "w" deletes old content
#"a" keeps old content and adds new data
#File must exist when using "r" mode

#8. Example Program

# Writing to file
with open("example.txt", "w") as f:
    f.write("Learning File I/O in Python")

# Reading from file
with open("example.txt", "r") as f:
    print(f.read())



# Summary :

#File I/O = Read + Write files
#Use open() with modes (r, w, a)
#Use with for safer code
#Helps in saving data permanently


# Real-Life Uses
#Saving user data
#Logging system events
#Reading configuration files
#Working with CSV/JSON files



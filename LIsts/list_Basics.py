#a list is a collection that can store multiple items in a single variable.
#You create a list using square brackets []:
#Lists can store: Integers, Strings, Floats, Booleans, Even other lists
#Lists are mutable, which means you can change them.
# u can append a new digit os str using name.append()
#numbers.remove(2)  # removes value 2
#numbers.pop()       # removes last item
#numbers.pop(0)      # removes item at index 0
#list.sort = sorts the list in ascending order
#list.insert (index,element) >> inserts an element at specific index



#Summary :   

#Lists store multiple items.
#Created using []
#Ordered (items keep position)
#Mutable (can change)
#Indexed starting at 0



list = [1,5,6,"Pandu", "ch", True] # declaration of list


print(list[0:5])  # accesing using index doesn't include end index like here , index 5 is not included


list.append("Naidu") # appends at the end of the list


print(list)

list.remove(5)

print(list) # removes the digit 5 and prints the list without it

length = len(list) # calculates the length of the list

print(length)# prints the length

num = [1,4,5,35]

for i in num :
    print(i) # prints the each element in the list in order that is in the list
    max(0,i) # checks the each element in the list to find the max value using max() built in function
    print(i) # prints the greatest value




add = sum(num) # calculates the sum of the digits in the list num

print (add)# prints the sum

reverse = num.reverse() #reverses the list (num)   #method 2: [::-1] more usseful

print(reverse) # prints the list in reverse order

duplicate = [1,2,3,2,33,4,4,2]

dup = set(duplicate) # converts the list into set which removes the duplicates , Method 2 : use loop

print(dup) # prints the list without duplicate elements


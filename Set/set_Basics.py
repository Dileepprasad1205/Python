# A set in Python is a collection of unique elements (no duplicates) and is unordered (no indexing).
my_set1 = {1, 2, 3, 4} #sample set creation
print(my_set1)

my_set2 = set([1, 2, 3]) # another method of declaring set ([])
print(type(my_set2)) #gives the type of the variable my_set2

#Important Properties : 
#No duplicate values
#No indexing (you can’t access like my_set[0])
#Mutable (you can add/remove items)
#Unordered (items may appear in any order)

s = {1, 2, 2}
print(s)   # Output: {1, 2} Here, duplicate values are skipped
s.add(3)   # add element 3 in set s using add() attribute
print(s)   # {1, 2, 3} 

s.remove(2)   # error if not found
s.discard(5)  # no error if not found  , Mostly used

print(s) # {1,3}

#**************************Union (Combine sets)************************

A = {1, 2}
B = {2, 3}
print(A | B)   # {1, 2, 3} combines a A & B and removes duplicates


#**************************Intersection (Common elements)************************

print(A & B)   # {2} gives elements that is in both sets

#**************************Difference************************

print(A - B)   # {1}


#**************************Symmetric Difference************************

print(A ^ B)   # {1, 3}


# | Method           | Description          |
# | ---------------- | -------------------- |
# | `add()`          | Adds element         |
# | `remove()`       | Removes element      |
# | `discard()`      | Removes safely       |
# | `clear()`        | Removes all elements |
# | `union()`        | Combines sets        |
# | `intersection()` | Common elements      |


# *******************************PRACTICE*********************************

# 1

set1 = {1,2}
print(set1)

#2

set1.add(3)
print(set1)

#3

set1.discard(2)
print(set1)

#4

list1 = [1,2,3,4,3,2,1]
duplicate = set(list1)
print(duplicate)

#5

P = {1,2,3}
Q = {3,4,5}
print(P|Q)

#6

print(P&Q)

#7

print(P-Q)

#8

A1 = {1, 2}
B1 = {3, 4}

if A1.isdisjoint(B1):
    print("No common elements")
else:
    print("Common elements exist")
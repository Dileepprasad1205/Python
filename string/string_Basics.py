 #[start:stop:step] = slicing
 #Split keyword is used to split words in a sentence
 #count() is a method (function) used with strings, lists, or tuples to count how many times a value appears.
 #An empy string can be created using str = ""
 #Frequency of a character can be found using set(name of the input)
 #sorted word is used to change the order of the word
 #anagram = arranging the characters in a given word in alphabetic order
 #max is the built-in function to find the largest of the (maximum) value
 #title() = Capitalizes first letter of every word
 


name = str(input())
dance = str(input())

length = len(name)
print(length)
upp = str.upper(name)
print(upp)
lwr = str.lower(name)
print(lwr)



for ch in name :
    print(ch)


count = 0

for ch in name :
    if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
        count +=1

print (count)

num = 0

for ch in name :
    if(ch != "a" and ch != "e" and ch != "i" and ch != "o" and ch != "u"):
        num +=1

print (num)

reverse = name[::-1]  # Sclicing

print(reverse)

reversed = dance[::-1]     

if dance == reversed :
    print("Polindrome")
else :
    print("Not a polindrome")


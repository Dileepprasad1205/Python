#Function ->> a function is a block of reusable code that performs a specific task. 
              # Instead of writing the same code again and again, 
              # you can “wrap” it inside a function and call it whenever needed.


#Why Use Functions?

#Functions help you:

#Avoid repeating code
#Make programs easier to read
#Break problems into smaller parts




#Declaring a  function

def greet():       #def → tells Python you're defining a function ,greet is the name of the function
    print("Hello!") # work in the function to do when the function is called

greet() # function call

#   Functions with Parameters


def greet(name): # it takes name as an input from the user
    print("Hello,", name) 

greet("pandu") # passing of the parameter and calling function

#    Functions with Return Values

def add(a, b): # also has two paramters
    return a + b # return a+b when the function is called

print(add(2,3)) # function call


#   Default Parameters

def greet(name="Dileep"):  # if the parameter is not given during the function call it uses the default parameter 
    print("Hello,", name)


greet()          # uses default
greet("Pandu")     # overrides default


#******************************************Practice_Questions******************************************

#1 : EVEN OR ODD ?

def e_or_o (num) :
    if (num % 2 == 0) :
        print(num," Is an Even number")
    else :
        print(num," Is an Odd number")

e_or_o(int(input("enter any number :")))



#2 : Maximum of Two Numbers 

def max(x,y) :
    if(x > y) :
        print(x," is the greatest number")
    else :
        print(y," is the greatest number ")

a = int(input("enter the first number : "))
b = int(input("enter the second number : "))

max(a,b)
    

#3  : Sum of List
def add(my_list) :
    sum = 0
    
    for i in my_list :
        sum = sum + i
    return sum
        
my_list = [1,2,3,4,5]

print(add(my_list))

#4  : String Length

#Method 1 : without using len() attribute
def length1(name) :
    count = 0
    for ch in name :
        count = count + 1
    
    return count

string1 = str(input("enter the string : "))

print(length1(string1))

#Method 2 :

def length2(name2) :
    return len(name2)


string2 = str(input("enter the string : "))

print(length2(string2))


#5 : Count Vowels

def count_vowels(word) :
    cout = 0
    vowels = "aeiouAEIOU"

    for ch in word :
        if ch in vowels:
            cout = cout + 1
    return cout

Word = str(input("enter the string : "))

print (count_vowels(Word) , "vowels are in the word")

#6 : Factorial (using loop)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("enter any number : "))
print("Factorial of the given n is : ", factorial(n))

#7  : Reverse a String


def reverse_string(s):
    return s[::-1]
    
s = str(input("enter any string : "))
print("reversed string is : ",reverse_string(s))

#8  : check if the number is prime or not 


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int (input("Enter any number : "))

print(is_prime(n))
        

#9  :  List of Squares


def squares(square_list) :
    res = []
    for i in square_list :
        res.append(i*i)
        
    return res


square_list = [1,2,3,4,5]

print(squares(square_list))



#10 : Remove Duplicates

def remove_duplicates(lst):
    r = []
    for item in lst:
        if item not in r:
            r.append(item)
    return r


lst = [1,2,2,3,4,3,3,3,5,2]

print(remove_duplicates(lst))


#11 : Palindrome Check

def is_palindrome(s):
    return s == s[::-1]

ss = input("Enter anything to check : ")
print(is_palindrome(ss))



#12 : second largest number 

def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

l = [1,2,3,1,24,534,5333]

print(second_largest(l))



#13 :  Count Words

def count_words(sentence):
    words = sentence.split()
    return len(words)


sentence =  str(input("Enter any sentence to find its length : "))
print(count_words(sentence))

#14 : Find Common Elements

def common_elements(lst1, lst2):
    lis = []
    for item in lst1:
        if item in lst2 and item not in lis:
            lis.append(item)
    return lis

lst1 = [1,2,3,2,12,3]
lst2 = [12,31,22,3,4,21]

print(common_elements(lst1,lst2))


#15  : Simple Calculator


def calculator(p, q, op):
    if op == "+":
        return p + q
    elif op == "-":
        return p - q
    elif op == "*":
        return p * q
    elif op == "/":
        if q != 0:
            return p / q
        else:
            return "Division by zero error"
    else:
        return "Invalid operator"
    

p = int(input("Enter any  number : "))
q = int(input("Enter any  number : "))


op = str(input("Enter any operator in +,-,*,/ : "))

print(calculator(p,q,op))
#Loops in Python are used to repeat a block of code multiple times until a condition is met.
#They help you avoid writing the same code again and again.

#***********************************FOR LOOP***************************************

# Used when you know how many times you want to repeat something.

#syntax :

set1 = {1,2,3}

for i in set1:# code block
    print(i)

# Example : 

for i in range(5):
    print(i) # prints the numbers from 0-4 using range(5) here , 5 is not included


#***********************************WHILE LOOP***************************************

#syntax : 

#   while condition:
    # code block

# Example : 

i = 0 # starting point else the loop will be infinite
while (i<=5):   #condition
    print(i)# code block
    i+=1 # increment of 1  means after checking the condition , if the condition is true it increments the i value by 1


#*****************************Loop Control Statements********************************

# break :  Stops the loop completely after meting it's condition

#Example :
   
for i in range(5):
    if i == 3:
        break
    print(i)


# continue : Skips the current iteration. after meting its condition

#Example :

for i in range(5):
    if i == 2:
        continue
    print(i)

#  pass : Does nothing (placeholder).

for i in range(3):
    pass


#*****************************Real-Life Example********************************


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# Key Points

#Use for loop → when iterations are known
#Use while loop → when condition-based
#Always be careful with while loops (can become infinite loops)




#*****************************Practice Questions********************************

#1 printing numbers from 1-10

for i in range (1,11) :
    print(i)

#2 printing even numbers between 1-20

i = 0

while i <= 20 :
    print(i)
    i+=2


#3 printing sum of the digits from 1-100

sum = 0
j = 1
while j<=100 :
    sum = sum + j
    j+=1

print(sum)

#4 pattern printing right angled triangle

for i in range(1, 6):
    print("*" * i)

#5 printing numbers from 10-1 

for i in range(10, 0, -1):  # syntax of the range is range (start , stop , step)
    print(i)


#6 count digits

num = 12345
count = 0

while num > 0:
    num //= 10
    count += 1

print(count)

#7 reverse a number

num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)

#8 prime number check

num = 6
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print(is_prime)

#9 Multiplication table

num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#10. Factorial

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)

#11 Fibonacci series

n = 7
a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b  # a = b , b = a+b 
    
#Recursion in Python is a programming technique where a function calls itself to solve a problem.

#Instead of solving the whole problem at once, recursion:

#Breaks the problem into smaller pieces
#Solves the smaller version
#Combines the results


#Basic Structure of a Recursive Function

#Every recursive function has two main parts:

#Base Case – Stops the recursion
#Recursive Case – The function calls itself

#************************************BASIC SYNTAX**********************************************

#def function_name(parameters):
#    if base_case_condition:
#       return result
#    else:
#        return function_name(smaller_problem)



#  Example 1: Factorial

def factorial(n):
    if n == 0:          # Base case
        return 1
    else:               # Recursive case
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


#  Example 2: Fibonacci Sequence

def fibonacci(n):
    if n <= 1:      # Base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8



#*******************************************Recursion vs Loop********************************************

#Loops are usually:

#More memory-efficient
#Faster

#Recursion is often:

#Cleaner
#Easier to understand for tree-like problems






#When to Use Recursion

#Recursion is useful for:

#Tree structures
#Graph traversal
#Divide-and-conquer algorithms
#Problems that can be defined in terms of themselves



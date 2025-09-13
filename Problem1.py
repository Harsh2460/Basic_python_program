# How to add two numbers in python.

# 1_method. Using the "+" operator
a = 20
b = 15

# Adding two numbers
res = a + b
print(res)

# 2_method. Using user input

# taking user input
a = input("First number: ")
b = input("Second number: ")

# Converting input to float and adding
res = float(a) + float(b)
print(res)

# 3_method. Using function
def add(a, b):
    return a + b

# initializing numbers
a = 15
b = 20

# calling function
res = add(a, b)
print(res)

# 4_method. Using lambda function
res = lambda a, b: a + b
print(res(35, 14))

# 5_method. Using operator.add
import operator
print(operator.add(5, 35))

# 6_method. Using sum()
print(sum([10, 5]))
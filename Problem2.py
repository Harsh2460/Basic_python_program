# Find maximum of two numbers in python.

# 1_method. Using max()
a = 11
b = 4

print(max(a, b))

# 2_method. Using ternary method
a = 14
b = 6

print(a if a > b else b)

# 3_method. Using if-else statement
a = 17
b = 8

if a > b:
    print(a)
else:
    print(b)

# 4_method. Using sort()
a = 7
b = 3

num = [a, b]
num.sort()
print(num[-1])
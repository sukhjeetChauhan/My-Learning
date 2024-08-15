name = 'John' # str
age = 35 #int
height = 6.2 #float
happy = True # boolean
l1 = [1,2,3,4] #list()
t1 = (1,2,'a', [5,6,7]) # tuple

#  to know type of each variable

print(type(name))
print(type(age))
print(type(height))
print(type(happy))
print(type(l1))
print(type(t1))

# format()

print(format(1/35, '.20f'))

# to solve equality operations in float nums

f1 = 0.3
f2 = 0.1
print(f1 == f2 * 3) # This will return false
# to solve this issue use isClose() method

from math import isclose
f3 = f2 * 3

print(isclose(f1,f3, abs_tol=0.01)) # this will return true

#  challenges

# challenge 1
# This script contains some syntax errors.
# Modify the script so that it runs without any errors.

best_friend = 'Anne'
print('My best friend is ', best_friend)

age = 18
print(age)

a, b = '10', '20'
print(a + b)

print('To comment a line of code you # at the beginning of the line.')


# challenge 2
# An IPv6 address is represented using 128 bits.

# Write a Python script that calculates how many IPv6 addresses are available. You can also include reserved IP addresses.

AVAILABLE_ADDRESSES = 2 ** 128
print(AVAILABLE_ADDRESSES)
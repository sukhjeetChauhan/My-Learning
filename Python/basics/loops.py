# Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.

x = int(input('Enter value of x:'))
y = int(input('Enter value of y:'))
count = 0

while x != 1:
  if x % y == 0:
     x = x / y
     count += 1
  else:
    print('x is not a power of y')
    break

else:
  print(f"x = y ** {count}")






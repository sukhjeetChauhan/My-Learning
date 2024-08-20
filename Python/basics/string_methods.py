my_str = 'I am learning Python'

# upper(), lower(), capitialize(), replace(), split(), join(), count(), find()
upper_str = my_str.upper()
lower_str = my_str.lower()
capitalize_str = my_str.capitalize()
replaced_str = my_str.replace(' ', '#')

print(upper_str,',',lower_str,',',capitalize_str,',',replaced_str)
print('#' * 30)

str_list = my_str.split()
hashed_str = "#".join(str_list)
print(str_list,',', hashed_str)
print('count:', my_str.lower().count('python'))
print('position of l:', my_str.find('l'))

# slicing the string

my_str_sliced = my_str[my_str.find('l'):]
print(my_str_sliced)
print(type(len(my_str)-1))
print(my_str[my_str.find('l'):len(my_str)])

# reversing a string

print(my_str[::-1])

# string challenge 1

# Consider the following string declaration which is part of the output of a Linux command.
# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

extract = my_str.removeprefix('wlo1 Link encap:Ethernet HWaddr').strip()
extract2 = my_str.split()[-1]
print(extract)
print(extract2)
print('#'* 30)
# challenge 2

# Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
# The user will be prompted to enter the value in ft.
# Display the value in cm with 2 decimals, formatted using an f-string.

# value_in_cms = f'The value entered by user is {(float(input("Enter your value here:")) * 30.48):.2f} cms'
# print(value_in_cms)
# print('#' * 30)

# Challenge #4

# Write a Python script that tests if a string is a palindrome.

# magic_str = input('Enter your string here: ')
# str_length = len(magic_str)
# mid_index = str_length // 2
# reverse_str = magic_str[mid_index:][::-1]
# print(magic_str[:mid_index + 1] == reverse_str)

print('#' * 30)
# ////////////////////////////////////////////////////////////////////
n = 12384756982
n_comma = f'{n:,}'

print(n_comma)

# print(n_comma.replace(',', '.'))
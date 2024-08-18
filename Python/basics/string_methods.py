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
#strings methods
# python3 strings and methods

# create a string
my_string = "Hello World"

# access a character in the string
print(my_string[0])

# print the length of the string
print(len(my_string))

# print the number of times a character appears in the string
print(my_string.count("l"))

# print the index of a character in the string
print(my_string.index("o"))

# print the string as all uppercase
print(my_string.upper())

# print the string as all lowercase
print(my_string.lower())

# print the string with the first letter of each word capitalized
print(my_string.title())

# print the string with the first letter capitalized
print(my_string.capitalize())

# print the string with all instances of a character replaced
print(my_string.replace("l", "L"))

# print the string with all instances of a character removed
print(my_string.replace("l", ""))

# separate the string into a list of strings
print(my_string.split(" "))
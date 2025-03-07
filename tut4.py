# Strings 
# --------------------------------------

# demo string 
value = "Hello world"
value2 = "hello world"

# 0. finding length
print(len(value))

# 1. slicing
second_name = value[6:12] #from ind_start(6) to ind_end(12)-1
print(second_name)

skip_slicing = value[0::2]
# take the whole ind_start to ind_end string and jump last_value characters in the string 
print(skip_slicing)

# 2. getting a certain character 
char = value[2]
print(char)

# 3. .endswith() and startswith.()
print(value.endswith('rld'))
print(value.startswith('Hel'))

# 4. .capitalize
print(value2.capitalize())

# 5. upper lower and title
print(value2.lower())
print(value2.upper())
print(value2.title())

# 6. .find()
print(value2.find('world'))

# 7. replace 
print(value2.replace('world', 'duniya'))

# 8. strip, lstrip, rstrip (removing whitespace)
value3 = "   hello world   "
print(value3.strip())  # Removes both leading and trailing spaces
print(value3.lstrip()) # Removes leading spaces
print(value3.rstrip()) # Removes trailing spaces

# 9. split() - splits a string into a list
print(value.split(" "))

# 10. join() - joins elements of a list into a string
words = ["Hello", "world"]
print("-".join(words))

# 11. count() - counts occurrences of a substring
print(value.count("l"))

# 12. isalnum(), isalpha(), isdigit()
alnum_str = "Hello123"
alpha_str = "Hello"
digit_str = "12345"
print(alnum_str.isalnum()) # True (letters + numbers)
print(alpha_str.isalpha()) # True (only letters)
print(digit_str.isdigit()) # True (only numbers)

# 13. isspace() - checks if a string contains only spaces
space_str = "   "
print(space_str.isspace())

# 14. swapcase() - swaps case of letters
print(value.swapcase())

# 15. zfill() - pads string with zeros on the left
num_str = "42"
print(num_str.zfill(5))  # Output: '00042'

# 16. rfind() - finds last occurrence of a substring
print(value.rfind("o"))

# 17. center() - centers a string with padding
print(value.center(20, "*"))

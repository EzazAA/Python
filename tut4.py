# Strings 
# [[][][][][][[][]][][][][][][][][]]

# demo string 
value = "Hello world"

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
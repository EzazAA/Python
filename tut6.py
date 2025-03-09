# List and tuples

# ----------
# Group of data 

# list --
fruits = ["Apples", "Oranges", "Bananas", "Kiwis"]
Info = ["Apples", "Oranges", "Bananas", "Kiwis", 0.5, 69, False, None]
print(fruits[0])  # Prints the first element in the list

# Lists are mutable 
fruits[2] = "Papayas"  # Changes the third element in the list
print(fruits)

# List methods 

# 1. .sort()
nums = [12, 32, 12, 5, 7, 36]
print(nums)  # Prints the original list
nums.sort()  # Sorts the list in ascending order
print(nums)  # Prints the sorted list

# 2. .append()
fruits.append("Mangoes")  # Adds "Mangoes" to the end of the list
print(fruits)

# 3. .reverse()
fruits.reverse()  # Reverses the order of the list
print(fruits)

# 4. .insert()
fruits.insert(1, "Strawberries")  # Inserts "Strawberries" at index 1
print(fruits)

# 5. .remove()
fruits.remove("Kiwis")  # Removes the first occurrence of "Kiwis" from the list
print(fruits)

# 6. .pop()
popped_fruit = fruits.pop()  # Removes and returns the last item in the list
print(fruits)
print("Popped fruit:", popped_fruit)  # Prints the popped item

# 7. .count()
apple_count = fruits.count("Apples")  # Counts the number of occurrences of "Apples" in the list
print("Number of Apples:", apple_count)

# 8. .index()
orange_index = fruits.index("Oranges")  # Returns the index of the first occurrence of "Oranges"
print("Index of Oranges:", orange_index)

# 9. .extend()
more_fruits = ["Grapes", "Pineapples"]
fruits.extend(more_fruits)  # Adds all elements from more_fruits to the end of the list
print(fruits)

# 10. .clear()
fruits.clear()  # Removes all elements from the list
print(fruits)

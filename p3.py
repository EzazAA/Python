# 1. 
userName  = input("Sir, What is your name? -")
print("Good Afternoon", userName)

# 2.

letter = '''    Dear Name
    You are selected
    date'''
date = input("What is today's date? - ")
print("\tDear" , userName, "\n\tYou Are selected\n", "\t",date)

# 2.1.
letter.replace("Name",userName)
letter.replace("date", date)
print(letter.replace("Name",userName).replace("date", date))

# 3.
string = "hello  world"
print(string.find("  "))

# 4.
print(string.replace("  ", "   "))

# 5.
letter2 = 'Dear sir, i wont be able to atttend your class due to illnes. Thanks'
print(letter2.replace(", ", ",\n\t").replace(". ", ".\n\t"))
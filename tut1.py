# Modules 
# Pre written Code that can be used in my code to improve efficiency - flask, django etc.

# Pip is the method that is used to install this things 
# `pip install <module-name>`

#   BUILT-IN/EXTERNAL MODULES
#  Module example - Pyjokes
import pyjokes

jokes = pyjokes.get_jokes()
for joke in jokes:
    print(joke)
# ------------------------------------------------ 
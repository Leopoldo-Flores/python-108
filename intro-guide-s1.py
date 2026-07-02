# ============================================
# 🐍 Python Basics - Session 1
# ============================================

# --- PRINTING TO THE TERMINAL ---
print("Hello World from Python!")   # No semicolons needed at the end of lines
print(2)                            # Printing a number
print(5 + 3)                        # Printing the result of a math operation
print(True)                         # Printing a boolean value

# Example of forgetting to save:
print("Didn't save")  # If you don’t save, changes won’t show up when you run the file

# Shortcuts:
# - Save file: Ctrl + S (Windows) or Cmd + S (Mac) 
# - Run last command in terminal: Up arrow + Enter


# --- COMMENTS ---
# This is a single-line comment. It won’t show up in the terminal.
# Comments are useful for explaining your code to others (or yourself later).
# You can also "comment out" code you don’t want to run:
# print("This won't run")

"""
This is a multi-line comment (docstring style).
Triple quotes let you write longer explanations.
"""


# --- VARIABLES AND CONCATENATION ---
name = "Angela"
age = 28
print(name)   # Prints the variable value

# Concatenation (joining strings with +)
# This will cause an error because age is an integer:
# print("My name is " + name + " and I am " + age + " years old.")

# Fix: convert age to a string with str()
print("My name is " + name + " and I am " + str(age) + " years old.")


# --- NAMING CONVENTIONS ---
# In JavaScript we often use camelCase, but in Python we use snake_case:
# firstName   →   first_name


# --- MORE VARIABLES ---
name = "Michael"
age = 46
middle_name = "John"
last_name = "Scott"
found = False   # Boolean variable

print(name)
print("My name is " + name + " and I am " + str(age) + " years old.")
print("Did he show up to class? " + str(found))


# --- MINI CHALLENGE 1 ---
"""
Write a short story using variables.
Steps:
2. Declare and initialize variables (strings and numbers)
3. Use print() and concatenation to tell the story
4. Run the program in the terminal
"""

# Example solution:
place = "Disneyland"
activity = "riding the rollercoaster"
members = 5
print("The last time I went to " + place + ", I had a great time " + activity + " with " + str(members) + " friends.")


# --- F-STRINGS ---
# Cleaner way to format strings
print(f"My name is {name}, and I am {age} years old.")

# Multi-line f-string
print(f"""
My name is: {name} {middle_name} {last_name}
I like programming in Python!
""")


# --- TYPE FUNCTION ---
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
print(type(True))   # <class 'bool'>


# --- CASTING (Changing Data Types) ---
print(20 + int("20"))   # 40
print(20 + age)         # 66
print(20 + 2.98)        # 22.98 


# --- INPUT FUNCTION ---
# input() lets the user type values into the terminal
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# input() always returns a string
print(type(input("Enter your age: ")))   # <class 'str'>

# Example: converting input to int
new_age = int(input("Enter your age: "))
print(age + new_age)


# --- MINI CHALLENGE 2 ---
"""
Pizza Calculator
    - Ask how many slices of pizza and how many people.
    - Use math operators to calculate slices per person.
    - Show the result with an f-string.
"""
slices = int(input("How many slices of pizza do you have? "))
people = int(input("How many people are sharing the pizza? "))
slices_per_person = slices / people
print(f"Each person gets {slices_per_person} slices of pizza.")


# --- Assignment#1 ---
# Dog Age Converter


print("\n--------- Dog Age Converter ---------\n")
dog_age_human = int(input("Enter your dog's age in human years: "))
dog_age_dog = dog_age_human * 7
print(f"Your dog is {dog_age_dog} years old in dog years!")
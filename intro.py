print("Hello World from Python!") #dont need to use semicolons at the end of lines in python 
print(2)
print(5+3)
print(True) 
print("Didn't save") #show this as en example of what happens when you don't save(it won't show up in terminal)
# shotcut for saving is ctrl + s (or cmd + s on Mac)
# shortcut for running code is up arrow + enter and it will run the last line of code you ran

#### This is a comment, \\\\\it won't show up in the terminal
# Comments are useful for explaining your code to others (or yourself in the future)
# You can also use comments to "comment out" code that you don't want to run
#### print("This won't run")

"""
This is a multi-line comment
You can use triple quotes to create multi-line comments
"""
# This is useful for explaining longer sections of code
 

####create a variable 
name = "angela"
age = 28
print(name) # run this
# concatination (putting things together) basically connecting by using + symbol
# print("My name is : " + name + ", and I am " + age + " years old.") 
# this will give an error because you can't concatinate a string and an integer, you can in javascript but not in python
# to fix this you need to convert the integer to a string using the str() function
print("My name is : " + name + ", and I am " + str(age) + " years old.")
# show them that hovering over str will show you what it does

"""
# explain that in javascript we use camelCase but in python we use snake_case
addingValues  adding_values #delete this after explaining
firstName    first_name #delete this after explaining
"""

####create a variable
name = "Michael"
age = 46
middle_name = "John" # ADD THIS # this is how snake_case looks in python
last_name = "Scott"   # ADD THIS
found = False      # ADD THIS #explain that variables can use all data types
print(name)
#### concatination 
print("My name is : " + name + ", and I am " + str(age) + " years old.")
print("Did he show up to the class? " + str(found)) #test found variable 
# this just returns the boolean value as a string

"""
10 min .md they dont have to type this MC1.md
# MINI CHALLENGE 1

Write a breife story using variables
And print the story in the terminal
You should use strings and numeric variables
on your story.
Note: The story can be just be 4 lines or sentences.
STR (Steps to Reproduce):
1. create a new file called story.py
2. Declare and initalize the variables
3. Use the print function to concatinate the story
4. Run the program in the terminal

point of challenge was to practice variables and print function and concatination
"""

# Solution
place = "disneyland"
activity = "riding the rollercoaster"
members = 5
print("The last time I went to " + place + ", I had a great time " + activity + " with " + str(members) + " of my friends.")



########## the f format
########## f"" or f""""""
# this helps clean up your code and makes it easier to read
print(f"My name is : {name}, and I am {age} years old.")
# it automatically converts age to a string so no need for str() function
# you do not need to use + symbol to concatinate
print(f""" 

asldkjt
      lkajsdf
{name}
                   im still in the f format


""") # you can use f format for triple quotes for multi-line strings

print(f""" 
My name is: {name} {middle_name} {last_name}
I like programming in Python
""")
# soo again you can use f format to replace concatination and make your 
# code cleaner and easier to read

### ///////// 20 min break /////////

### the type() function helps us to know what type of data a variable
print(type(name)) # <class 'str'>
print(type(age))  # <class 'int'>
print(type(True)) # <class 'bool'>

### Casting
### Helps us to convert different data types
### str() - converts from any data type to a string
### int() - converts from any data type to an integer
print(20+int("20")) # 40
print(20+age)  # 43
print(20+2.98) # 22.98 can even be used with decimals
# can be used for all data types

### input method
### is going to allow us to interact with the terminal and pass some values
### input() HIGHLIGHT IT AND READ
print(input("Enter your name here: ")) # this will show a prompt in the terminal
# basically it will pause the program and wait for the user to type something
# once the user types something and hits enter it will return that value as a string

print(type(input("Enter your age here: "))) # this will always return a string <class 'str'>

new_age = input("Enter your age here: ") # this will store the value in the variable new_age
print(age + int(new_age)) ### 23 + 20 = 43
# ASK what would happen if we try to add age + new_age
# run it to show them the error # this will give an error because you can't add an integer and a string
# to fix this we need to convert new_age to an integer using the int() function
new_age = int(input("Enter your age here: ")) # this will store the value in the variable new_age
print(int(age) + new_age) ### 23 + 20 = 43

# example of converting age to a string
# print(str(age) + new_age) # 2320 # bc adding both string just puts them together with no space
# if its numbers it will add them together if both are integers 

# little example of how it works
x = int(input("Enter a first value: "))
y = int(input("Enter a second value: "))
print(x+y) # this will add the two values together


#?  ==== MINI-CHALLENGE 1 ====
"""
Meme/Text Generator
    - Create 2 variables with funny words or phrases.
    - Use print() and math operators to combine them into funny messages.
    - Example: "Python + coffee = happy programmer".
"""
# ----- Example1 -----
# Variables with funny words/phrases
word1 = "Python"
word2 = "coffee"

# Combine them into a funny message using +
print(word1 + " + " + word2 + " = happy programmer")

# ----- Example2 -----
# Another example
thing1 = "Homework"
thing2 = "weekend"
print(thing1 + " - " + thing2 + " = sad student")


#? ===== MINI-CHALLENGE 2 ====
"""
Pizza Calculator
    - Ask how many slices of pizza and how many people.
    - Use math operators to calculate slices per person.
    - Show the result with an f-string.
"""
# ----- Example 1 -----
# Ask the user for input
slices = int(input("How many slices of pizza do you have? "))
people = int(input("How many people are sharing the pizza? "))

# Calculate slices per person
slices_per_person = slices / people

# Show the result with an f-string
print(f"Each person gets {slices_per_person} slices of pizza.")

#? ==== Assignment ====
"""
Dog Age Converter
    - Ask the user for their dog's age in human years.
    - Multiply by 7 to convert to "dog years".
    - Show the result with an f-string.
"""

print(" \n --------- Dog Age Converter ---------\n")

# Ask the user for their dog's age in human years 
dog_age_human = int(input("Enter your dog's age in human years: "))

# Convert to dog years (multiply by 7)
dog_age_dog = dog_age_human * 7

# Show the result with an f-string
print(f"Your dog is {dog_age_dog} years old in dog years!")


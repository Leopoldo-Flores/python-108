"""
loops

A for loop in Python is a control structure that lets you repeat a block of code for each item in a sequence 
(such as a list, string, tuple, dictionary, or a range of numbers).

❌It's used when you know how many times you want to repeat an action or when you want to process each element in a collection.


for variable in sequence:
    # Code block runs for each item in the sequence
"""
# Basic example
fruits = ["apple", "banana", "cherry"]


for fruit in fruits:
    print(fruit)

print("__________________________________")


for letter in "Leo":
    print(letter)

print("__________________________________")

# range() generates a sequence of numbers

for x in range(5): # hover over range and show that it stops
    print(x)  # Prints 0,1,2,3,4 Because range() only includes 
              # numbers that are strictly less than the stop value.
              # remember indexing starts at 0. soo 5 is actually 4 0,1,2,3,4
print("__________________________________")

# Start and end range
for x in range(2, 6):
    print(x)  # Prints 2,3,4,5

print("__________________________________")

for number in range(2, 6):  # 2 to 5
    print(number)

print("__________________________________")


for number in range(0, 10, 2):  # 0 to 8, step 2
    print(number)



"""
Mini-challenge
1. Ask the user to enter a number and store it in a variable called num.
2. Use a for loop with range(1, 11) to repeat 10 times (from 1 to 10).
3. Inside the loop, multiply num by the current loop value (i).
"""

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("__________________________________")


"""
WHILE LOOPS
A while loop repeats a block of code as long as a condition is True.
Be careful — if the condition never becomes False, you’ll get an INFINITE loop!

while condition:
    # Code block runs as long as condition is True
"""

count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Assignment opperator which increase count each time (so the loop eventually ends)

print("__________________________________")


# -------------------------------
# USING break TO STOP THE LOOP 
# -------------------------------
number = 0

while True:   # infinite loop
    print(number)
    number += 1
    if number == 3:
        break   # stop the loop when number reaches 3

print("__________________________________")

# -------------------------------
# USING continue TO SKIP AN ITERATION
# -------------------------------
count = 0 # initialize count at 0
while count < 5:
    count += 1
    if count == 3:
        continue  # skips 3
    print(count)

print("__________________________________")

# -------------------------------
# ELSE WITH WHILE
# -------------------------------
# The else block runs when the loop condition becomes False (not by break)

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished!")


print("__________________________________")


# Mini Challenge: Password Checker MC7.md
# 1. Ask the user to enter a password
# 2. Check if it's correct (password: "secret123") 
# 3. If it's wrong, print "Wrong! Try again." and ask again
# 4. When they enter the correct password, print "Access granted!"

# Solution:
password = ""                        # Start empty
while password != "secret123":       # Keep looping while password is wrong
    password = input("Enter password: ")
    if password != "secret123":      # If wrong
        print("Wrong! Try again.")

# Once they finally type "secret123", the while condition (password != "secret123") becomes false, so the loop stops.
print("Access granted!")

print("__________________________________")

# -------------------------------
#  FOR LOOPS
# -------------------------------
# A for loop is used for looping over a sequence:
# a list, tuple, dictionary, string, etc.

# Loop through a list
fruits = ["apple", "banana", "cherry"] # convert to tuple use () not []
for fruit in fruits: # for each fruit in the list fruits
    print(fruit)

print("__________________________________")

# Loop through a string
for letter in "hello": # ask them what they think it would print
    print(letter)

print("__________________________________")



# Step (skip numbers)
for x in range(0, 10, 2): # start at 0, go up to 10, step by 2
    print(x)  # Prints 0,2,4,6,8

print("__________________________________")

# -------------------------------
# ELSE IN FOR LOOP
# -------------------------------
for x in range(3): #
    print(x)
else: # runs when loop is done
    print("Loop done!")

print("__________________________________")

# -------------------------------
# BREAK and CONTINUE in for loops
# -------------------------------
for x in range(10):
    if x == 5:
        continue  # Skip 5 because continue goes to the next iteration
    if x == 8:
        break     # Stop loop completely
    print(x)


# Mini challenge: Count how many words have 5 or more letters MC8.md
# 1. create a list with some words
# 2. use a while loop to go through each word
# 3. count how many words have 5 or more letters (hint: len())
# 4. print the result

# Solution:
words = ["apple", "hi", "banana", "dog", "computer", "sun"]
count = 0                        # Start with 0 words counted because we haven't checked any yet

for word in words:               # Go through each word in the list
    if len(word) >= 5:           # If word has 5 or more letters
        count += 1               # Add 1 to the counter

print("There are", count, "long words.")


"""
loops

A for loop in Python is a control structure that lets you repeat a block of code for each item in a sequence 
(such as a list, string, tuple, dictionary, or a range of numbers).

❌It's used when you know how many times you want to repeat an action or when you want to process each element in a collection.


for variable in sequence:
    # Code block runs for each item in the sequence
"""

# Loop through a list
fruits = ["apple", "banana", "cherry"] # convert to tuple use () not []
for fruit in fruits: # for each fruit in the list fruits
    print(fruit)

print("__________________________________")

# Loop through a string
for letter in "hello": # ask them what they think it would print
    print(letter)

print("__________________________________")

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
-------------------------------
MINI CHALLENGE: FOR LOOP
-------------------------------
Student Score Analyzer
1. Create a list called scores containing:
[85, 92, 67, 78, 95, 88]
2. Create a variable called passing_scores and set it to 0.
3. Use a for loop to go through each score.
4. If the score is 70 or higher:
- Add 1 to passing_scores
- Print "<score> passed"
5. Otherwise:
- Print "<score> failed"
6. After the loop finishes:
- Print the total number of passing scores.
BONUS:
Print "Excellent class performance!"
if 5 or more students passed.
"""

scores = [85, 92, 67, 78, 95, 88]

passing_scores = 0

for score in scores:

    if score >= 70:
        passing_scores += 1
        print(score, "passed")
    else:
        print(score, "failed")

print("Passing students:", passing_scores)

if passing_scores >= 5:
    print("Excellent class performance!")
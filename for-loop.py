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

print("__________________________________")

# -------------------------------
# ENUMERATE() -- get the index AND the value
# -------------------------------
# Sometimes you need to know WHICH position an item is at while
# you loop through it. enumerate() gives you both at once instead
# of having to track a counter variable yourself.

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)   # 0 apple, 1 banana, 2 cherry

# You can even choose where the counting starts
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")   # 1. apple, 2. banana, 3. cherry

print("__________________________________")

# -------------------------------
# ZIP() -- loop through two lists together
# -------------------------------
# zip() pairs up items from multiple sequences by position,
# so you can loop through them side by side.

names = ["Leo", "Alex", "Nina"]
scores = [92, 85, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

print("__________________________________")

# -------------------------------
# NESTED FOR LOOPS (a loop inside a loop)
# -------------------------------
# The inner loop runs COMPLETELY for every single pass of the outer loop.
# Common use case: working with a grid, a multiplication table, or
# comparing every item in one list against every item in another.

for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})", end="  ")
    print()  # move to a new line after each row finishes

print("__________________________________")


"""
Mini-challenge- Multiplication table
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
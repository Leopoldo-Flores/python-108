# -------------------------------
#  LISTS IN PYTHON
# -------------------------------
# Lists are used to store MULTIPLE items in a single variable.
# Think of them like a "container" that can hold many values at once.
# Example: a shopping list, or a list of student names.

# Lists are written with square brackets [ ]

my_list = [10, 20, 30, 40, 50]
print(my_list)

# Lists can contain different data types
mixed_list = [1, "apple", 3.5, True]
print(mixed_list) 

# -------------------------------
# WHERE LISTS FIT IN (vs tuples, sets, dictionaries)
# -------------------------------
# Python has 4 built-in ways to store a collection of items.
# They all look similar at first, but each one exists for a different reason:
#
#   LIST        [ ]   ordered   duplicates OK   MUTABLE (can change)
#   TUPLE       ( )   ordered   duplicates OK   IMMUTABLE (can't change)
#   SET         { }   unordered duplicates NOT allowed   mutable
#   DICTIONARY  { }   ordered (key:value)   keys must be unique   mutable
#
# Use a LIST when:
#   - The order of items matters (first, second, third...)
#   - You expect to ADD, REMOVE, or CHANGE items later
#   - Example: a to-do list, a queue of players, scores that keep growing
#
# Compare that to:
#   - TUPLE  → order matters but data should NEVER change (e.g. days of the week)
#   - SET    → order doesn't matter, but duplicates should be impossible (e.g. unique visitor IDs)
#   - DICT   → you need to look something up by a name/key instead of a position (e.g. a student's grade by their name)
#
# Lists are the most flexible and most commonly used collection —
# that's why they're a great place to start, but knowing WHEN to
# reach for a tuple/set/dict instead is just as important as
# knowing the syntax.

# -------------------------------
# ACCESSING ITEMS BY INDEX
# -------------------------------
# (Indexing starts at 0)

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # First item (apple)
print(fruits[1])  # Second item (banana)

# You can also use NEGATIVE indexes to count from the end
print(fruits[-1])  # Last item (cherry)

# -------------------------------
# SLICING A LIST
# -------------------------------
# Slicing lets you grab a RANGE of items using [start:stop]
# It includes "start" but stops BEFORE "stop" (just like range()).

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])   # [2, 3, 4]        → index 2 up to (not including) 5
print(numbers[:4])    # [0, 1, 2, 3]     → from the beginning up to index 4
print(numbers[6:])    # [6, 7, 8, 9]     → from index 6 to the end
print(numbers[-3:])   # [7, 8, 9]        → the last 3 items
print(numbers[::2])   # [0, 2, 4, 6, 8]  → every 2nd item (step of 2)

# -------------------------------
# MODIFYING LIST ITEMS
# -------------------------------
fruits[1] = "mango"   # Change banana -> mango
print(fruits)

# -------------------------------
# ADDING ITEMS
# -------------------------------
fruits.append("orange")   # Adds ONE item to the END
print(fruits)

fruits.insert(1, "kiwi")  # Adds at a SPECIFIC position (index 1)
print(fruits)

fruits.extend(["grape", "pear"])  # Adds MULTIPLE items to the end
print(fruits)                     # (append() would add the whole list as ONE item instead)

# -------------------------------
# REMOVING ITEMS
# -------------------------------
fruits.remove("apple")    # Removes by VALUE (the first match it finds)
print(fruits)

fruits.pop()               # Removes the LAST item and returns it
print(fruits)

fruits.pop(0)               # Removes the item at a SPECIFIC index (here, index 0)
print(fruits)

# fruits.clear()            # Would remove EVERYTHING, leaving an empty list []

# -------------------------------
# LOOPING THROUGH A LIST
# -------------------------------
for fruit in fruits:
    print(fruit)

# -------------------------------
# CHECK IF ITEM EXISTS
# -------------------------------
if "mango" in fruits:
    print("Yes, mango is in the list!")

# -------------------------------
# LIST LENGTH
# -------------------------------
print(len(fruits))  # Number of items in list

# -------------------------------
# USEFUL LIST METHODS
# -------------------------------
numbers = [4, 2, 9, 1, 7]

print(numbers.count(2))   # How many times 2 appears in the list -> 1
print(numbers.index(9))   # The INDEX where 9 first appears -> 2

numbers.sort()             # Sorts the list in place (smallest to largest)
print(numbers)             # [1, 2, 4, 7, 9]

numbers.sort(reverse=True)  # Sort largest to smallest
print(numbers)               # [9, 7, 4, 2, 1]

numbers.reverse()            # Flips the current order of the list
print(numbers)

numbers_copy = numbers.copy()  # Makes a real COPY (see note below on why this matters)
print(numbers_copy)

# -------------------------------
# WHY .copy() MATTERS (a common beginner bug)
# -------------------------------
# If you do "new_list = numbers", you do NOT get a copy —
# both variable names point to the SAME list in memory.
# Changing one changes the other!

original = [1, 2, 3]
not_a_copy = original       # both names point to the same list
not_a_copy.append(4)
print(original)             # [1, 2, 3, 4]  <- original changed too! probably not what you wanted

real_copy = original.copy()  # this makes an independent copy
real_copy.append(99)
print(original)              # unaffected
print(real_copy)             # [1, 2, 3, 4, 99]

# -------------------------------
# LIST COMPREHENSIONS (a quicker way to build a list)
# -------------------------------
# Instead of writing a for loop to build a new list, you can do it in one line.

squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)  # [1, 4, 9, 16, 25]

# The exact same result, written as a list comprehension:
squares_comprehension = [x * x for x in range(1, 6)]
print(squares_comprehension)  # [1, 4, 9, 16, 25]

# You can even add a condition
even_only = [x for x in range(1, 11) if x % 2 == 0]
print(even_only)  # [2, 4, 6, 8, 10]



# -------------------------------
#  MINI CHALLENGE: THE GROCERY LIST
# -------------------------------
# You're building a grocery list app.

# 1. Create a list called "groceries" with at least 5 items.
# 2. Print the first and last item using indexing.
# 3. Use slicing to print just the first 3 items.
# 4. Add "eggs" to the end of the list using append().
# 5. Insert "milk" at the very beginning of the list.
# 6. Remove one item using remove().
# 7. Check if "bread" is in the list — print a message either way.
# 8. Sort the list alphabetically and print it.
# 9. Print how many items are in the final list.



# -------------------------------
#  SOLUTION: THE GROCERY LIST
# -------------------------------

# Create the list of groceries
groceries = ["apples", "bread", "cheese", "chicken", "rice"]

# Access the first and last item
print("First item:", groceries[0])
print("Last item:", groceries[-1])

# Slice the first 3 items
print("First 3 items:", groceries[:3])
 
# Add "eggs" to the end
groceries.append("eggs")

# Insert "milk" at the beginning (index 0)
groceries.insert(0, "milk")
print("After adding milk and eggs:", groceries)

# Remove "cheese" from the list
groceries.remove("cheese")

# Check if "bread" is still in the list
if "bread" in groceries:
    print("Bread is on the list!")
else:
    print("We're out of bread!")

# Sort alphabetically
groceries.sort()
print("Sorted list:", groceries)

# Total number of items
print("Total items:", len(groceries))



"""
-------------------------------
MINI CHALLENGE: HIGH SCORE BOARD
-------------------------------
You are building a leaderboard for a game.

1. Create a list called "scores" with at least 6 integer scores.
2. Use a list comprehension to create "bonus_scores" where every
   score has 10 points added to it.
3. Sort "bonus_scores" from highest to lowest.
4. Print the TOP 3 scores using slicing.
5. Use count() to check how many times a specific score appears.
6. Remove the LOWEST score from the list using pop() and the index
   of the minimum value (hint: use .index(min(list))).
7. Print the final list and how many scores remain.
"""


# -------------------------------
#  SOLUTION: HIGH SCORE BOARD
# -------------------------------

# Create the list of scores
scores = [85, 92, 67, 78, 95, 88]

# List comprehension: add 10 bonus points to every score
bonus_scores = [score + 10 for score in scores]

# Sort from highest to lowest
bonus_scores.sort(reverse=True)
print("Bonus scores (sorted):", bonus_scores)

# Top 3 scores using slicing
print("Top 3 scores:", bonus_scores[:3])

# Count how many times a specific score appears
print("Times 105 appears:", bonus_scores.count(105))

# Remove the lowest score
lowest_index = bonus_scores.index(min(bonus_scores))
bonus_scores.pop(lowest_index)

# Final results
print("Final scores:", bonus_scores)
print("Total scores remaining:", len(bonus_scores))
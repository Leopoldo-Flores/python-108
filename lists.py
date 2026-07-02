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

# You can access list items by their INDEX number
# (Indexing starts at 0)

fruits = ["apple", "banana", "cherry"] 
print(fruits[0])  # First item (apple) 
print(fruits[1])  # Second item (banana)

# You can also use NEGATIVE indexes to count from the end
print(fruits[-1])  # Last item (cherry)

# -------------------------------
# MODIFYING LIST ITEMS
# -------------------------------
fruits[1] = "mango"   # Change banana → mango
print(fruits)

# -------------------------------
# ADDING ITEMS
# -------------------------------
fruits.append("orange")   # Adds to the END
print(fruits)

fruits.insert(1, "kiwi")  # Adds at a SPECIFIC position
print(fruits)

# -------------------------------
# REMOVING ITEMS
# -------------------------------
fruits.remove("apple")    # Removes by value
print(fruits)

fruits.pop()              # Removes last item 
print(fruits)

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

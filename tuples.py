# -------------------------------
#  TUPLES IN PYTHON
# -------------------------------
# Tuples are just like lists — they can store multiple items.
# BUT! Tuples are IMMUTABLE (you can’t change them after creation).

# Tuples are written with ROUND brackets ( )
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# -------------------------------
# ACCESSING ITEMS
# -------------------------------
print(my_tuple[0])   # First item
print(my_tuple[-1])  # Last item

# -------------------------------
# CHECK IF ITEM EXISTS
# -------------------------------
if "banana" in my_tuple:
    print("Yes, banana is in the tuple!")

# -------------------------------
# LENGTH OF A TUPLE
# ------------------------------- 
print(len(my_tuple))

# -------------------------------
# SINGLE ITEM TUPLE 
# -------------------------------
# You must add a comma at the end or Python won’t recognize it as a tuple.
single = ("apple",)
print(type(single))   # tuple
not_tuple = ("apple") # this is just a string
print(type(not_tuple))

# -------------------------------
# NESTED TUPLES
# -------------------------------
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combined = (tuple1, tuple2)
print(combined)


# -------------------------------
#  MINI CHALLENGE: THE TRAVEL BAG
# -------------------------------
# You’re packing for a trip! You have a tuple that stores the items you’re taking.

# 1. Create a tuple called "travel_bag" with at least 5 items (e.g. "shirt", "toothbrush", etc.)
# 2. Print the SECOND and FOURTH items in your bag.
# 3. Check if "shoes" is in your travel bag — if it is, print "You're ready to walk!"
#     otherwise, print "You forgot your shoes!"
# 4. Make a new tuple called "essentials" with 3 must-have items.
# 5. Combine both tuples into one called "final_bag".
# 6. Print how many total items you now have using len().
# 7. Print the last item in your "final_bag".



# -------------------------------
#  SOLUTION: THE TRAVEL BAG   MC3.md
# -------------------------------

# Create a tuple that holds all the items you plan to take on your trip
# Tuples use parentheses () and cannot be changed once created
travel_bag = ("shirt", "toothbrush", "wallet", "hat", "charger")

# Access items in a tuple using their index number
# Index starts at 0 → so [1] is the second item
print("Second item:", travel_bag[1]) 
print("Fourth item:", travel_bag[3])

# Use "in" to check if something exists in the tuple
if "shoes" in travel_bag:
    print("You're ready to walk!")  # Runs if "shoes" is in the tuple
else:
    print("You forgot your shoes!") # Runs if "shoes" is NOT in the tuple

# Create another tuple with essential items
essentials = ("passport", "phone", "cash")

# Combine both tuples using the + operator
# This creates a NEW tuple since tuples are immutable
final_bag = travel_bag + essentials

# len() gives the total number of items inside the tuple
print("Total items:", len(final_bag))

# Negative index [-1] means the last item in the tuple
print("Last item:", final_bag[-1])



"""
# -------------------------------
#  MINI CHALLENGE: CLASS QUIZ ANALYZER
# -------------------------------
# You are analyzing quiz scores stored in a tuple.

# 1. Create a tuple called "quiz_scores" with at least 6 integer scores.
# 2. Print the FIRST 3 scores and the LAST 3 scores using slicing.
# 3. Print the HIGHEST and LOWEST score using built-in functions.
# 4. Check if ANY score is below 70:
#    - If yes, print "Warning: At least one failing score!"
#    - Otherwise print "All students passed!"
# 5. Create a new tuple called "bonus_scores" where each score is increased by 5.
# 6. Combine "quiz_scores" and "bonus_scores" into a tuple called "final_scores".
# 7. Print the total number of scores in "final_scores".
# 8. Print the LAST score in "final_scores".
"""


# -------------------------------
#  SOLUTION: CLASS QUIZ ANALYZER
# -------------------------------

# Create tuple of quiz scores
quiz_scores = (82, 75, 91, 68, 88, 95)

# Print first 3 and last 3 using slicing
print("First 3 scores:", quiz_scores[:3])
print("Last 3 scores:", quiz_scores[-3:])

# Highest and lowest score
print("Highest score:", max(quiz_scores))
print("Lowest score:", min(quiz_scores))

# Check if any score is below 70
if any(score < 70 for score in quiz_scores):
    print("Warning: At least one failing score!")
else:
    print("All students passed!")

# Create bonus_scores tuple (add 5 to each score)
bonus_scores = tuple(score + 5 for score in quiz_scores)

# Combine tuples
final_scores = quiz_scores + bonus_scores

# Total number of scores
print("Total scores:", len(final_scores))

# Last score in final tuple
print("Last score:", final_scores[-1])
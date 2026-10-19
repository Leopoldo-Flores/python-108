# -------------------------------
#  TUPLES IN PYTHON
# -------------------------------
# Tuples are just like lists — they can store multiple items.
# BUT! Tuples are IMMUTABLE (you can’t change them after creation).

# Tuples are written with ROUND brackets ( )
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# -------------------------------
# WHY USE A TUPLE INSTEAD OF A LIST?
# -------------------------------
# Both store multiple items in order, but a tuple LOCKS the data
# so it can't be changed by accident. Use a tuple when the data
# represents something that should stay constant, like:
#   - the days of the week
#   - GPS coordinates (latitude, longitude)
#   - a date (year, month, day)
# If you find yourself wanting to .append() or .remove() items,
# that's a sign you probably want a LIST instead of a tuple.

# -------------------------------
# ACCESSING ITEMS
# -------------------------------
print(my_tuple[0])   # First item
print(my_tuple[-1])  # Last item

# -------------------------------
# TUPLES CAN'T BE CHANGED (try it!)
# -------------------------------
# my_tuple[0] = "kiwi"      # TypeError: 'tuple' object does not support item assignment  <- uncomment to show
# my_tuple.append("kiwi")   # AttributeError: 'tuple' object has no attribute 'append'

# Need to "change" one? Convert to a list, change the list, convert back:
temp_tuple = ("apple", "banana", "cherry")
temp_list = list(temp_tuple)
temp_list[0] = "kiwi"
temp_tuple = tuple(temp_list)
print(temp_tuple)   # ('kiwi', 'banana', 'cherry')

# -------------------------------
# JOINING, SLICING AND LOOPING
# -------------------------------
more = ("date", "elderberry")
print(my_tuple + more)   # + joins tuples into a NEW tuple
print(more * 2)          # * repeats a tuple
print(my_tuple[1:])      # slicing works just like lists
for item in my_tuple:    # and so do loops
    print(item)

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
# COUNT AND INDEX (the two methods tuples DO have)
# -------------------------------
# Because tuples are immutable, they don't have methods like
# append(), remove(), or sort(). They only have count() and index().

letters = ("a", "b", "a", "c", "a")
print(letters.count("a"))  # How many times "a" appears -> 3
print(letters.index("c"))  # The index where "c" first appears -> 3

# -------------------------------
# TUPLE UNPACKING
# -------------------------------
# You can "unpack" a tuple's items directly into separate variables.
# This is a very common Python pattern.

coordinates = (10, 20)
x, y = coordinates
print(x)  # 10
print(y)  # 20

person = ("Leo", 22, "Computer Science")
name, age, major = person
print(f"{name} is {age} years old and studies {major}")

"""
===============================================================
MINI CHALLENGE (SIMPLE · 5-10 min): THE TRAVEL BAG
===============================================================
You’re packing for a trip! You have a tuple that stores the items you’re taking.

1. Create a tuple called "travel_bag" with at least 5 items (e.g. "shirt", "toothbrush", etc.)
2. Print the SECOND and FOURTH items in your bag.
3. Check if "shoes" is in your travel bag — if it is, print "You're ready to walk!"
    otherwise, print "You forgot your shoes!"
4. Make a new tuple called "essentials" with 3 must-have items.
5. Combine both tuples into one called "final_bag" (hint: the + operator).
6. Print how many total items you now have using len().
7. Print the last item in your "final_bag".
"""


# -------------------------------
#  SOLUTION: THE TRAVEL BAG
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
===============================================================
MINI CHALLENGE (HARDER · ~10 min): CLASS QUIZ ANALYZER
===============================================================
You are analyzing quiz scores stored in a tuple.

1. Create a tuple called "quiz_scores" with at least 6 integer scores.
2. Print the FIRST 3 scores and the LAST 3 scores using slicing.
3. Print the HIGHEST and LOWEST score using built-in functions.
4. Check if ANY score is below 70:
   - If yes, print "Warning: At least one failing score!"
   - Otherwise print "All students passed!"
5. Create a new tuple called "bonus_scores" where each score is increased by 5.
   (Tuples can't be changed -- so how could you BUILD a new one?)
6. Combine "quiz_scores" and "bonus_scores" into a tuple called "final_scores".
7. Print the total number of scores in "final_scores".
8. Print the LAST score in "final_scores".
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

# Check if any score is below 70 (loop + a True/False flag)
has_failing = False
for score in quiz_scores:
    if score < 70:
        has_failing = True

if has_failing:
    print("Warning: At least one failing score!")
else:
    print("All students passed!")
# (Shortcut for later:  if any(score < 70 for score in quiz_scores): ...)

# Tuples can't be changed, so build a LIST of the new scores, then convert it to a tuple
bonus_list = []
for score in quiz_scores:
    bonus_list.append(score + 5)
bonus_scores = tuple(bonus_list)
# (Shortcut for later:  bonus_scores = tuple(score + 5 for score in quiz_scores))

# Combine tuples
final_scores = quiz_scores + bonus_scores

# Total number of scores
print("Total scores:", len(final_scores))

# Last score in final tuple
print("Last score:", final_scores[-1])
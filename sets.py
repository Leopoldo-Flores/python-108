# -------------------------------
#  SETS IN PYTHON
# -------------------------------
# Sets are used to store multiple items in a single variable.
# Sets are UNORDERED, UNINDEXED, and have NO DUPLICATES.

# Sets are written with curly brackets { }
fruits = {"apple", "banana", "cherry"}
print(fruits)

# -------------------------------
# NO DUPLICATES ALLOWED
# -------------------------------
fruits = {"apple", "banana", "apple"}
print(fruits)  # "apple" only appears once

# -------------------------------
# CHECK IF ITEM EXISTS
# -------------------------------
print("banana" in fruits)

# -------------------------------
# ADDING ITEMS
# -------------------------------
fruits.add("orange")
print(fruits)

# -------------------------------
# ADDING MULTIPLE ITEMS
# -------------------------------
fruits.update(["kiwi", "mango"])
print(fruits)

# -------------------------------
# REMOVING ITEMS
# -------------------------------
fruits.remove("banana")  # Removes "banana"
print(fruits)

# If you’re not sure an item exists, use discard() to avoid errors
fruits.discard("papaya")

# -------------------------------
# SET OPERATIONS (like in math)
# -------------------------------
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # Combine both (no duplicates)
print(set1.intersection(set2)) # Common elements
print(set1.difference(set2))   # What’s only in set1



# -------------------------------
#  MINI CHALLENGE: PARTY GUEST LIST MC4.md
# -------------------------------
# You’re organizing a party! You have two sets of guests.

# 1. Create two sets:
#     - invited_friends = {"Alex", "Sam", "Leo", "Nina"}
#     - rsvped = {"Nina", "Sam", "Jordan"}

# 2. Print:
#     - Everyone who was invited (union)
#     - Everyone who said they’re coming (rsvped)
#     - Who hasn’t replied yet (difference)

# 3. Add two new names to invited_friends.
# 4. One of the people canceled — remove them from rsvped.
# 5. Print how many total confirmed guests are attending.
# 6. Check if "Leo" is still coming — print a message depending on the result.

# -------------------------------
#  SOLUTION: PARTY GUEST LIST
# -------------------------------

# Create two sets for people invited and those who RSVP'd
# Sets use curly braces {} and automatically remove duplicates
invited_friends = {"Alex", "Sam", "Leo", "Nina"}
rsvped = {"Nina", "Sam", "Jordan"}

# Print both sets
print("All invited:", invited_friends)
print("RSVP'd:", rsvped)

# difference() shows items in invited_friends but NOT in rsvped
print("Not yet replied:", invited_friends.difference(rsvped))

# Add multiple new names to invited_friends with update()
invited_friends.update(["Taylor", "Maya"])

# Remove a name from rsvped using remove()
# (If the name doesn’t exist, Python will show an error) 
rsvped.remove("Jordan")
 
# len() gives how many items are inside the set
print("Total confirmed guests:", len(rsvped))

# Check if a specific guest is in the set
if "Leo" in rsvped:
    print("Leo is coming!")          # True branch
else:
    print("Leo hasn’t replied yet.") # False branch
 





"""
# -------------------------------
#  MINI CHALLENGE: STUDY GROUPS
# -------------------------------
# Two study groups are preparing for an exam.

# 1. Create two sets:
#     - group_a = {"Leo", "Sam", "Alex", "Nina"}
#     - group_b = {"Nina", "Jordan", "Sam", "Taylor"}

# 2. Print:
#     - All students participating in either group (union)
#     - Students who are in BOTH groups (intersection)
#     - Students who are only in group_a (difference)

# 3. Add "Maya" to group_a.

# 4. Remove "Jordan" from group_b.

# 5. Print the total number of unique students across both groups.

# 6. If "Nina" is in both groups,
#       print("Nina is helping both groups!")
#    Otherwise,
#       print("Nina is only in one group.")

# 7. Print the final version of both sets.
"""

# Create the sets
group_a = {"Leo", "Sam", "Alex", "Nina"}
group_b = {"Nina", "Jordan", "Sam", "Taylor"}

# Union = everyone
print("All students:", group_a.union(group_b))

# Intersection = students in both groups
print("In both groups:", group_a.intersection(group_b))

# Difference = only in group_a
print("Only in Group A:", group_a.difference(group_b))

# Add a student
group_a.add("Maya")

# Remove a student
group_b.remove("Jordan")

# Count unique students
all_students = group_a.union(group_b)
print("Total unique students:", len(all_students))

# Check if Nina is in both groups
if "Nina" in group_a and "Nina" in group_b:
    print("Nina is helping both groups!")
else:
    print("Nina is only in one group.")

# Print final sets
print("Group A:", group_a)
print("Group B:", group_b)
# -------------------------------
#  SETS IN PYTHON
# -------------------------------
# Sets are used to store multiple items in a single variable.
# Sets are UNORDERED, UNINDEXED, and have NO DUPLICATES.
# You can't CHANGE an individual item inside a set (there's no index to point at it),
# but you CAN add new items and remove items.
# NOTE: because a set has no order, the order it prints in can change from run to run.

# Sets are written with curly brackets { }
fruits = {"apple", "banana", "cherry"}
print(fruits)

# -------------------------------
# WHY USE A SET INSTEAD OF A LIST?
# -------------------------------
# Use a set when you don't care about order and you need to
# guarantee there are NO duplicates, or when you need to quickly
# compare two groups of items (who's in both? who's only in one?).
# Examples: unique visitor IDs, tags on a post, ingredients that
# overlap between two recipes.
# A set also checks "is this item in here?" much faster than a
# list does once you get into large amounts of data -- that's a
# side benefit, but the main reason to reach for a set is
# "I need uniqueness" or "I need union/intersection/difference."

# -------------------------------
# NO DUPLICATES ALLOWED
# -------------------------------
fruits = {"apple", "banana", "apple"}
print(fruits)  # "apple" only appears once

# -------------------------------
# set() -- REMOVE DUPLICATES FROM A LIST (the most common real-world use!)
# -------------------------------
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique_emails = set(emails)
print(unique_emails)
print(len(unique_emails))    # 3 different emails
print(list(unique_emails))   # turn it back into a list if you need a list

# GOTCHA: {} makes an empty DICTIONARY, not an empty set. Use set() for an empty set.
print(type({}))      # <class 'dict'>
print(type(set()))   # <class 'set'>

# Sets can only hold items that can't change: numbers, strings and tuples are fine,
# but a list or dictionary inside a set will give an error.

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
print(set1.difference(set2))   # What's only in set1
print(set1.symmetric_difference(set2))  # Everything EXCEPT what's shared
print({1, 2}.issubset(set1))            # True -> every item of {1, 2} is inside set1

# -------------------------------
# FROZENSET (a "locked" set)
# -------------------------------
# A frozenset works just like a set, but it's IMMUTABLE -- once
# created, you can't add or remove items. You won't use these often
# as a beginner, but it's good to know they exist for the same
# reason tuples exist alongside lists: sometimes you want to
# guarantee your data can't be changed.
locked_set = frozenset(["a", "b", "c"])
print(locked_set)
# locked_set.add("d")  # This would raise an AttributeError

"""
-------------------------------
MINI CHALLENGE (SIMPLE · 5-10 min): PARTY GUEST LIST
-------------------------------
You’re organizing a party! You have two sets of guests.

1. Create two sets:
    - invited_friends = {"Alex", "Sam", "Leo", "Nina"}
    - rsvped = {"Nina", "Sam", "Jordan"}
2. Print:
    - Everyone involved: invited OR RSVP'd (union) -- Jordan RSVP'd but was never invited!
    - Everyone who said they’re coming (rsvped)
    - Who hasn’t replied yet (difference)
3. Add two new names to invited_friends.
4. One of the people canceled — remove them from rsvped.
5. Print how many total confirmed guests are attending.
6. Check if "Leo" is still coming — print a message depending on the result.
"""

# -------------------------------
#  SOLUTION: PARTY GUEST LIST
# -------------------------------

# Create two sets for people invited and those who RSVP'd
# Sets use curly braces {} and automatically remove duplicates
invited_friends = {"Alex", "Sam", "Leo", "Nina"}
rsvped = {"Nina", "Sam", "Jordan"}

# Print both sets
print("Everyone involved:", invited_friends.union(rsvped))
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
===============================================================
MINI CHALLENGE (HARDER · ~10 min): STUDY GROUPS
===============================================================
Two study groups are preparing for an exam.

1. Create two sets:
    - group_a = {"Leo", "Sam", "Alex", "Nina"}
    - group_b = {"Nina", "Jordan", "Sam", "Taylor"}
2. Print:
    - Students who are in BOTH groups (intersection)
    - Students who are in exactly ONE group (symmetric difference)
3. The exam sign-in sheet is a LIST with repeats (some people signed twice):
       signed_in = ["Leo", "Nina", "Leo", "Maya", "Nina", "Sam"]
   Use a set to print how many DIFFERENT students showed up.
4. Print which students from group_a did NOT show up.
5. Some people who showed up aren't in either group. Find who they are.
   (hint: combine the two groups first, then compare with who showed up)
6. If nobody is unregistered, print "Everyone belongs to a group!"
   Otherwise print "Unregistered students:" followed by their names.
"""

group_a = {"Leo", "Sam", "Alex", "Nina"}
group_b = {"Nina", "Jordan", "Sam", "Taylor"}

print("In both groups:", group_a.intersection(group_b))
print("In exactly one group:", group_a.symmetric_difference(group_b))

signed_in = ["Leo", "Nina", "Leo", "Maya", "Nina", "Sam"]
showed_up = set(signed_in)                    # the set removes the repeats
print("Different students who showed up:", len(showed_up))

print("Group A students who did NOT show up:", group_a.difference(showed_up))

all_registered = group_a.union(group_b)
unregistered = showed_up.difference(all_registered)

if len(unregistered) == 0:
    print("Everyone belongs to a group!")
else:
    print("Unregistered students:", unregistered)
# -------------------------------
#  DICTIONARIES IN PYTHON
# -------------------------------
# Dictionaries store data in KEY: VALUE pairs.
# Think of them like a mini database or a real-life dictionary (word → meaning).

# Written with curly brackets { }

student = {
    "name": "Leo",
    "age": 22,
    "major": "Computer Science"
}

print(student)
 
# -------------------------------
# ACCESSING ITEMS
# -------------------------------
print(student["name"])     # Access by key
print(student.get("major")) # Another way to access

# -------------------------------
# ADDING NEW ITEMS
# -------------------------------  
student["graduation_year"] = 2025
print(student)

# -------------------------------
# CHANGING VALUES
# -------------------------------
student["age"] = 23
print(student)

# -------------------------------
# REMOVING ITEMS
# -------------------------------
student.pop("major")  # Removes "major"
print(student)

# -------------------------------
# CHECK IF A KEY EXISTS
# -------------------------------
if "name" in student:
    print("Key 'name' exists in the dictionary!")

# -------------------------------
# NESTED DICTIONARY
# -------------------------------
students = {
    "student1": {"name": "Leo", "age": 22},
    "student2": {"name": "Alex", "age": 21}
}
print(students["student1"]["name"])  # Access nested value



# -------------------------------
#  MINI CHALLENGE: STUDENT REPORT CARD  MC2.md
# -------------------------------
# You need to store and analyze a student's grades.

# 1. Create a dictionary called "report_card" with keys:
#     - "name"
#     - "subject"
#     - "grades" (use a tuple with 3 numbers)
# Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}

# 2. Print the student's name and subject.
# 3. Calculate the average of the 3 grades (HINT: use sum() and len()).
# 4. Add a new key called "average" with the calculated result.
# 5. If the average is 90 or above → print "Excellent!"
#     If between 70 and 89 → print "Good job!"
#     Otherwise → print "Needs improvement!"
# 6. Remove the "subject" key and print the updated dictionary.



# -------------------------------
#  SOLUTION: STUDENT REPORT CARD
# -------------------------------

# Create a dictionary to store info about a student
# Uses {key: value} pairs 
report_card = {
    "name": "Leo",
    "subject": "Math",
    "grades": (90, 85, 88)  # Tuple to store 3 test scores
}

# Access dictionary values using their keys
print("Student:", report_card["name"])
print("Subject:", report_card["subject"])

# Calculate the average using sum() and len()
# sum adds all grades, len counts how many there are
avg = sum(report_card["grades"]) / len(report_card["grades"])

# Add a new key/value to the dictionary
report_card["average"] = avg

# Use if, elif, else to check grade performance
if avg >= 90:
    print("Excellent!")        # Runs if average is 90 or more
elif avg >= 70:
    print("Good job!")         # Runs if between 70–89
else:
    print("Needs improvement!")# Runs if below 70

# Remove a key/value pair using pop()
report_card.pop("subject")

# Print the updated dictionary to show the final result
print("Updated report card:", report_card)
 


"""
# -------------------------------
# MINI CHALLENGE: PLAYER PROFILE
# -------------------------------
# You are creating a simple player profile for a game.

# 1. Create a dictionary called "player" with the keys:
#     - "username"
#     - "level"
#     - "stats"
#
# The "stats" key should store another dictionary containing:
#     - "health"
#     - "attack"
#
# Example:
# {
#     "username": "Leo",
#     "level": 5,
#     "stats": {
#         "health": 100,
#         "attack": 25
#     }
# }

# 2. Print the player's username and level.

# 3. Increase the player's level by 1.

# 4. Add a new key called "gold" and give the player 500 gold.

# 5. If the player's attack is 30 or higher:
#       print("Strong player!")
#    Otherwise:
#       print("Needs more training!")

# 6. Remove the "health" stat from the nested dictionary.

# 7. Print the updated player dictionary.
"""

# Create the player dictionary
player = {
    "username": "Leo",
    "level": 5,
    "stats": {
        "health": 100,
        "attack": 25
    }
}

# Print username and level
print("Username:", player["username"])
print("Level:", player["level"])

# Increase level by 1
player["level"] += 1

# Add gold
player["gold"] = 500

# Check attack power
if player["stats"]["attack"] >= 30:
    print("Strong player!")
else:
    print("Needs more training!")

# Remove health from nested dictionary
player["stats"].pop("health")

# Print updated dictionary
print("Updated Player:", player)




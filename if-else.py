"""
if-else statement 

An if-else statement in Python is a conditional control structure that lets you decide which block 
of code to run depending on whether a condition is True or False.

The if block runs only if the condition evaluates to True.
•  If the condition is False, the else block runs instead.
•  You can also add elif (else if) blocks to check multiple conditions in sequence

if condition:
    - Code block runs if condition is True
elif another_condition:
    - Code block runs if the first condition is False
    - and this condition is True
else:
    - Code block runs if none of the above conditions are True

❌
Conditional statements let us make decisions in code.
The computer checks if something is True or False, then runs specific code.
It lets you check *another condition* if the first one is NOT true.
It gives your program more than two possible outcomes.

if → checks a condition
elif → (else if) checks another condition if the first is False
else → runs if all other conditions are False
"""
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# -------------------------------
# SHORT HAND IF STATEMENT
# -------------------------------
# You can write it all in one line if you want

if x > 5: print("x is greater than 5")

# -------------------------------
# SHORT HAND IF...ELSE
# -------------------------------
print("Even") if x % 2 == 0 else print("Odd")

# -------------------------------
# NESTED IF STATEMENTS
# -------------------------------
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# The word nested literally means “inside of something else.”
# So in programming, a nested statement is when you put one block 
# of code inside another block.

# Think of it like a box inside a box  —
# the outer box runs first, and then the inner box runs only if the 
# outer one allows it. 

# -------------------------------
# COMBINING CONDITIONS
# -------------------------------
age = 18

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old")

"""
Mini challenge

1. Ask the user to enter a number from 0-100 and store it in a variable called "score".
2. If the score is 90 or above, print "Grade: A".
3. If the score is between 80-89, print "Grade: B".
4. If the score is between 70-79, print "Grade: C".
5. Otherwise, print "Grade: F".

❌6. Create a variable "passed" — set it to True if score >= 70, otherwise False.
 BONUS: If passed is True, print "Congratulations!", otherwise print "Try again!"

"""

# Solution
# Ask the user for their score
score = int(input("Enter your score (0-100): "))

# Determine the grade
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Check if they passed (using a short-hand if/else) 
# passed = True if score >= 70 else False

# # BONUS: Message based on pass/fail
# if passed:
#     print("Congratulations!")
# else:
#     print("Try again!")

 
"""
Mini challenge

1. Ask the user to enter today's temperature in Fahrenheit and store it in a variable called temperature.
2. Use if-elif-else statements to classify the temperature:
    If temperature >= 86, print "It's hot outside!"
    If temperature >= 68 and temperature < 86, print "The weather is nice."
    If temperature >= 50 and temperature < 68, print "It's a bit chilly."
    Otherwise, print "It's cold!"
3. Create a variable called jacket:
    Set it to True if temperature < 59, otherwise False.
4. Bonus: If jacket is True, print "Better wear a jacket!", otherwise print "No jacket needed."
"""

temperature = int(input("Enter today's temperature in Fahrenheit: "))

# 2. Classify the temperature using if-elif-else
if temperature >= 86:   # ~30°C
    print("It's hot outside!")
elif temperature >= 68 and temperature < 86:   # ~20–29°C
    print("The weather is nice.")
elif temperature >= 50 and temperature < 68:   # ~10–19°C
    print("It's a bit chilly.")
else:
    print("It's cold!")

# 3. Create a variable 'jacket'
# jacket = temperature < 59   # ~15°C
if temperature < 59:
    jacket = True
else:
    jacket = False

# 4. Bonus: Print a message depending on whether a jacket is needed
if jacket == True:
    print("Better wear a jacket!")
else:
    print("No jacket needed.")







"""
Mini Challenge

1. Ask the user to enter their age and store it in a variable called age.
2. Ask the user if they have a valid ID.
   (The user should enter "yes" or "no".)
   Store the answer in a variable called has_id.

3. Determine admission rules:
    - If age is 21 or older AND has_id is "yes":
        print "Access Granted"
    - If age is 21 or older BUT has_id is "no":
        print "Access Denied - ID Required"
    - If age is between 18 and 20 inclusive:
        print "Access Limited"
    - Otherwise:
        print "Access Denied - Too Young"

4. Create a variable called can_enter:
    Set it to True only if the user is 21 or older AND has_id is "yes".
    Otherwise set it to False.

5. BONUS:
    If can_enter is True:
        print "Welcome inside!"
    Otherwise:
        print "Please see the front desk."

6. EXTRA BONUS:
    If the user enters a negative age,
    print "Invalid age entered."
"""

# 1. Get user input
age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

# 6. Input validation
if age < 0:
    print("Invalid age entered.")

else:

    # 3. Determine admission status
    if age >= 21 and has_id == "yes":
        print("Access Granted")

    elif age >= 21 and has_id == "no":
        print("Access Denied - ID Required")

    elif age >= 18:
        print("Access Limited")

    else:
        print("Access Denied - Too Young")

    # 4. Create boolean variable
    can_enter = age >= 21 and has_id == "yes"

    # 5. Bonus message
    if can_enter:
        print("Welcome inside!")
    else:
        print("Please see the front desk.")
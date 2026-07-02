# -------------------------------
#  OPERATORS IN PYTHON
# -------------------------------
# Operators are like "symbols" or "shortcuts"
# that tell the computer to do something with values (numbers, text, etc).
# Operators - are used to perform operations on variables and values

# We have the following Types of Operators:
# 1. Arithmetic (math stuff)
# 2. Assignment (put values into a variable)
# 3. Comparison (check if things are the same or different)
# 4. Logical (combine true/false conditions)
# 5. Identity (check if two things are the *same object*)
# 6. Membership (check if something is inside a list/sequence)

# 1. ARITHMETIC OPERATORS - used with numeric valus to perform common 
# mathematical operations
# NOTE: "res" is just a variable that stores the RESULT of the operation.
 
x = 1
y = 2
res = 0

res = x + y   # ➕ Addition (1 + 2 = 3)
print(res)
 
res = x - y   # ➖ Subtraction (1 - 2 = -1)
print(res)

res = x * y   # ✖️ Multiplication (1 * 2 = 2)
print(res)

res = x / y   # ➗ Division (1 / 2 = 0.5)
print(res)

res = x % y   # MODULUS → remainder after division (1 % 2 = 1)
print(res)

res = x ** y  # EXPONENTIATION → x to the power of y (1 ** 2 = 1)
print(res)

res = x // y  # FLOOR DIVISION → divide and drop the decimal (1 // 2 = 0)
print(res)

# 2. ASSIGNMENT OPERATORS - used to assign values to variables
# = means "put this value inside the (variable)"
# +=, -=, *=, /= are shortcuts.

x = 5
x += 5  # same as: x = x + 5 → (x becomes 10)
x -= 3  # same as: x = x - 3 → (x becomes 7)
x *= 3  # same as: x = x * 3 → (x becomes 21)
x /= 3  # same as: x = x / 3 → (x becomes 7.0)

# 3. COMPARISON OPERATORS
# Comparison - Used to compare two values
# same as the if else file

# == (equal to), != (not equal), > (greater), < (less), >=, <=

# 4. LOGICAL OPERATORS - used to combine conditional statements
# Used with True/False value like conditions.
# and → both must be True
# or → at least one must be True
# not → flips True to False (and vice versa)

x = 3
y = 10
z = 3

print(x == y and y == z)  # False, because both conditions are NOT true
print(x == y or y == z)   # True, because at least one condition is true
print(not x == y)         # True, because x == y is False, and NOT flips it

# 5. IDENTITY OPERATORS - used to compare the objects, not if they're equal 
# but if they're actually the same object with the same memory location
# is → checks if two things are the exact same object in memory
# is not → checks if they are NOT the same

x = 3
y = 3
print(x is y)       # Returns True if both variables are the same object
print(x is not y)   # Returns True if both variables are not the same object


# 6. MEMBERSHIP OPERATORS- used to test if a sequence is presented in an object
# in → checks if something exists inside a sequence (list, string, etc)
# not in → checks if something does NOT exist inside

x = [1, 2, 3, 4, 5]  # this is a list
# Lists are used to store multiple items in a single variable. acnd are created using square brackets []

print(4 in x)     # True, because 4 is inside the list
print(9 not in x) # True, because 9 is NOT inside the list

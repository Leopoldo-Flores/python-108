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

# 1. ARITHMETIC OPERATORS - used with numeric values to perform common
# mathematical operations
# NOTE: "res" is just a variable that stores the RESULT of the operation.

x = 7
y = 2
res = 0

res = x + y   # ➕ Addition (7 + 2 = 9)
print(res)

res = x - y   # ➖ Subtraction (7 - 2 = 5)
print(res)

res = x * y   # ✖️ Multiplication (7 * 2 = 14)
print(res)

res = x / y   # ➗ Division (7 / 2 = 3.5) -> / always gives a decimal
print(res)

res = x % y   # MODULUS → the REMAINDER after dividing (7 % 2 = 1)
print(res)    # handy trick: n % 2 == 0 means n is even

res = x ** y  # EXPONENTIATION → x to the power of y (7 ** 2 = 49)
print(res)

res = x // y  # FLOOR DIVISION → divide and drop the decimal (7 // 2 = 3)
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
z = 10

print(x == y and y == z)  # False, because "and" needs BOTH sides True (x == y is False)
print(x == y or y == z)   # True, because y == z is True ("or" needs only ONE)
print(not x == y)         # True, because x == y is False, and NOT flips it

# 5. IDENTITY OPERATORS - used to compare the objects, not if they're equal
# but if they're actually the same object with the same memory location
# is → checks if two things are the exact same object in memory
# is not → checks if they are NOT the same

x = [1, 2, 3]
y = [1, 2, 3]   # a second list that happens to have the same items
z = x           # z is NOT a copy: it points to the very same list as x

print(x == y)       # True  → same VALUES
print(x is y)       # False → two separate lists in memory
print(x is z)       # True  → same object
print(x is not y)   # True
# TIP: use == to compare values (numbers, strings...). The most common real use
# of "is" is checking for nothing:  if value is None:
# (Careful: 3 is 3 happens to be True because Python caches small numbers - don't rely on it)


# 6. MEMBERSHIP OPERATORS - used to test if a value is present in a sequence/object
# in → checks if something exists inside a sequence (list, string, etc)
# not in → checks if something does NOT exist inside

x = [1, 2, 3, 4, 5]  # this is a list
# Lists are used to store multiple items in a single variable and are created using square brackets []

print(4 in x)     # True, because 4 is inside the list
print(9 not in x) # True, because 9 is NOT inside the list
print("a" in "banana")  # True -> works on strings too


# ===============================================================
#  MINI CHALLENGE (SIMPLE · 5-10 min): TIP CALCULATOR
# ===============================================================
# Three friends split a restaurant bill. (No if statements needed!)
#
# 1. Create variables: bill = 48.50, tip_percent = 20, people = 3
# 2. Calculate the tip amount (bill * tip_percent / 100).
# 3. Calculate the total with the tip, then how much EACH person pays.
# 4. Print the per-person amount with an f-string (2 decimals: {value:.2f}).
# 5. Print True/False: does each person pay MORE than $20? (comparison operator)


# ----- SOLUTION: TIP CALCULATOR -----
bill = 48.50
tip_percent = 20
people = 3

tip = bill * tip_percent / 100
total = bill + tip
each = total / people

print(f"Each person pays ${each:.2f}")
print(each > 20)   # comparison operators give a True/False answer


# ===============================================================
#  MINI CHALLENGE (HARDER · ~10 min): MOVIE MARATHON PLANNER
# ===============================================================
# You're planning a movie marathon. Use ONE operator from EVERY group below.
# (No if statements needed -- just print the True/False results.)
#
# 1. Create three variables for movie lengths in minutes: 95, 120, 110.
#    Start total_minutes at 0 and add each movie using +=  (assignment operator)
# 2. Convert total_minutes to hours and minutes
#    (hint: which operators give "how many whole hours" and "what's left over"?)
#    Print it like:  The marathon is 5h 25m
# 3. Print whether the marathon is longer than 300 minutes. (comparison)
# 4. has_snacks = True, has_drinks = False.
#    Print whether you're fully ready (snacks AND drinks), whether you have at
#    least one of them (OR), and whether you're missing drinks (NOT).  (logical)
# 5. snacks = "popcorn candy nachos"
#    Print whether "popcorn" is in snacks, and whether "soda" is NOT in snacks. (membership)


# ----- SOLUTION: MOVIE MARATHON PLANNER -----
movie1 = 95
movie2 = 120
movie3 = 110

total_minutes = 0
total_minutes += movie1
total_minutes += movie2
total_minutes += movie3          # 325

hours = total_minutes // 60      # floor division -> whole hours
minutes = total_minutes % 60     # modulus -> what's left over
print(f"The marathon is {hours}h {minutes}m")

print(total_minutes > 300)       # True

has_snacks = True
has_drinks = False
print(has_snacks and has_drinks)   # False -> not fully ready
print(has_snacks or has_drinks)    # True  -> at least one
print(not has_drinks)              # True  -> missing drinks

snacks = "popcorn candy nachos"
print("popcorn" in snacks)         # True
print("soda" not in snacks)        # True


# ===============================================================
#  BONUS (only AFTER you've taught if/else): MOVIE TICKET DISCOUNT
# ===============================================================
# 1. Create variables: ticket_price = 12, has_coupon = True, is_member = False
# 2. Apply a $3 discount if has_coupon is True.
# 3. If has_coupon AND is_member are both True, apply an EXTRA $2 discount.
# 4. If the final price is less than $10 print "Great deal!", otherwise "Still a fair price."
# 5. Check if "popcorn" is in a list called concession_items -- print a message either way.

ticket_price = 12
has_coupon = True
is_member = False

if has_coupon:
    ticket_price -= 3   # same as: ticket_price = ticket_price - 3

if has_coupon and is_member:
    ticket_price -= 2

if ticket_price < 10:
    print("Great deal!")
else:
    print("Still a fair price.")

print(f"Final ticket price: ${ticket_price}")

concession_items = ["popcorn", "soda", "candy", "nachos"]

if "popcorn" in concession_items:
    print("Popcorn is available!")
else:
    print("Sorry, no popcorn today.")
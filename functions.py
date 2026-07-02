"""
functions

A function is a block of code that only runs when it is called.
We can pass data to functions (parameters), and they can return data as a result.

def function_name(parameters):
    # Code block (indented)
    # Perform actions using the parameters
    return value   # Optional

# Why use functions?
# - To avoid repeating code
# - To organize code into small, reusable pieces
# - To make programs easier to read and maintain
"""
# -------------------------------
# 1. Simple function without parameters
# -------------------------------
# "def" means we are DEFINING a function.
# It won’t run until we CALL it by its name.

def my_function():
    print("This is my function")  # This line runs when the function is called

# Calling the function
my_function()  

 
# -------------------------------
# 2. Another simple function
# -------------------------------
def other_function():
    print("This is another function!")

other_function()


# -------------------------------
# 3. Functions with parameters
# -------------------------------
# Parameters allow us to pass information into a function.

def print_full_name(first_name, last_name):
    # f-string = formatted string, lets us insert variables inside text
    print(f"The name is: {first_name} {last_name}")

# Example call (uncomment to run):
# print_full_name("Leo", "Flores")


# -------------------------------
# 4. Functions that return values
# -------------------------------
# Instead of just printing, functions can send back (return) data.

def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"  # Sends back the full name as text

# Store the returned value in a variable:
full_name = get_full_name("Leo", "Flores")
print(full_name)


# Functions with Default Parameters

# A default parameter means the function will use that value 
# if no argument is provided when calling the function.

def greet(name="Student"):
    print(f"Hello, {name}! Welcome to class.")

# Calling with no argument → uses the default
greet()   # Output: Hello, Student! Welcome to class.

# Calling with an argument → overrides the default
greet("Leo")   # Output: Hello, Leo! Welcome to class.




"""
# -------------------------------
# MINI CHALLENGE: MOVIE TICKET PRICE
# -------------------------------

# Create a function called calculate_ticket_price().
#
# 1. The function should accept:
#       - age
#       - is_student (default value = False)
#
# 2. Ticket pricing rules:
#       - Under 13 years old → $8
#       - 13 to 64 years old → $12
#       - 65 and older → $10
#
# 3. If is_student is True,
#       subtract $2 from the ticket price.
#
# 4. Return the final ticket price.
#
# 5. Call the function twice:
#       - One regular customer
#       - One student
#
# 6. Print the returned prices.
"""

def calculate_ticket_price(age, is_student=False):

    if age < 13:
        price = 8
    elif age >= 65:
        price = 10
    else:
        price = 12

    if is_student:
        price -= 2

    return price

ticket1 = calculate_ticket_price(30)
ticket2 = calculate_ticket_price(20, True)

print("Regular Ticket: $", ticket1)
print("Student Ticket: $", ticket2)





"""
# -------------------------------
# MINI CHALLENGE: PASSWORD CHECKER
# -------------------------------

# Create a function called check_password().
#
# 1. The function should accept one parameter:
#       - password
#
# 2. Inside the function:
#       - If the password length is 8 or more:
#             return "Strong Password"
#
#       - If the password length is between 5 and 7:
#             return "Medium Password"
#
#       - Otherwise:
#             return "Weak Password"
#
# 3. Ask the user to enter a password.
#
# 4. Call the function and store the returned result.
#
# 5. Print the result.
#
# BONUS:
# If the password contains an exclamation mark (!),
# print "Special character detected!"
"""

def check_password(password):

    if len(password) >= 8:
        return "Strong Password"

    elif len(password) >= 5:
        return "Medium Password"

    else:
        return "Weak Password"


user_password = input("Enter a password: ")

result = check_password(user_password)

print(result)

if "!" in user_password:
    print("Special character detected!")
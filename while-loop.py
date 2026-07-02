
"""
WHILE LOOPS
A while loop repeats a block of code as long as a condition is True.
Be careful — if the condition never becomes False, you’ll get an INFINITE loop!

while condition:
    # Code block runs as long as condition is True
"""

count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Assignment opperator which increase count each time (so the loop eventually ends)

print("__________________________________")


# -------------------------------
# USING break TO STOP THE LOOP 
# -------------------------------
number = 0

while True:   # infinite loop
    print(number)
    number += 1
    if number == 3:
        break   # stop the loop when number reaches 3

print("__________________________________")

# -------------------------------
# USING continue TO SKIP AN ITERATION
# -------------------------------
count = 0 # initialize count at 0
while count < 5:
    count += 1
    if count == 3:
        continue  # skips 3
    print(count)

print("__________________________________")

# -------------------------------
# ELSE WITH WHILE
# -------------------------------
# The else block runs when the loop condition becomes False (not by break)

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished!")


print("__________________________________")


# Mini Challenge: Password Checker MC7.md
# 1. Ask the user to enter a password
# 2. Check if it's correct (password: "secret123") 
# 3. If it's wrong, print "Wrong! Try again." and ask again
# 4. When they enter the correct password, print "Access granted!"

# Solution:
password = ""                        # Start empty
while password != "secret123":       # Keep looping while password is wrong
    password = input("Enter password: ")
    if password != "secret123":      # If wrong
        print("Wrong! Try again.")

# Once they finally type "secret123", the while condition (password != "secret123") becomes false, so the loop stops.
print("Access granted!")

print("__________________________________")



"""
-------------------------------
MINI CHALLENGE: WHILE LOOP
-------------------------------
Guess the Secret Number
1. Create a variable called secret_number
and set it equal to 7.
2. Ask the user to guess the number.
3. Use a while loop to keep asking until
they guess correctly.
4. If the guess is too low:
print "Too low!"
5. If the guess is too high:
print "Too high!"
6. When the user guesses correctly:
print "Correct!"
BONUS:
Count how many guesses the user needed.
"""

secret_number = 7

guess = -1
attempts = 0

while guess != secret_number:

    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

print("Correct!")
print("Attempts:", attempts)



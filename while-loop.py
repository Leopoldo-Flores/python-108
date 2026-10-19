"""
WHILE LOOPS
A while loop repeats a block of code as long as a condition is True.
Be careful — if the condition never becomes False, you’ll get an INFINITE loop!
(If your program gets stuck, press Ctrl + C in the terminal to stop it.)

while condition:
    # Code block runs as long as condition is True
"""

count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Assignment operator which increases count each time (so the loop eventually ends)

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

# -------------------------------
# WHILE LOOPS WITH LISTS
# -------------------------------
# "while my_list:" keeps looping as long as the list still has items in it
tasks = ["wash dishes", "do homework", "walk dog"]

while tasks:
    current = tasks.pop()      # pop() removes (and gives back) the LAST item
    print("Doing:", current)
print("All tasks done!")

print("__________________________________")

# -------------------------------
# HANDLING BAD INPUT (try / except)
# -------------------------------
# int("abc") crashes the program with a ValueError.
# try / except lets us CATCH the error and keep the program running.
while True:
    answer = input("Enter a whole number: ")
    try:
        number = int(answer)     # if this line crashes, Python jumps to "except"
        break                    # it worked! leave the loop
    except ValueError:
        print("That's not a whole number, try again.")

print(f"Thanks! You entered {number}")


print("__________________________________")


# MINI CHALLENGE (SIMPLE · 5-10 min): Password Gate
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
===============================================================
MINI CHALLENGE (HARDER · ~10 min): WHILE LOOP
===============================================================
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
BONUS 1:
Count how many guesses the user needed.
BONUS 2:
Make the secret number RANDOM from 1 to 10 so it can't be memorized.
(hint: put "import random" at the top of the file and look up random.randint)
"""

secret_number = 7
# BONUS 2 -> put "import random" at the very top, then use: secret_number = random.randint(1, 10)

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
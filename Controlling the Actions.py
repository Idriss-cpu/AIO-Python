import random
import datetime as dt
# from typing import Counter
# Controlling the Actions.
sun = "down"
if sun == "down":
    print("Good night")
print("I am here" + "\n")
total = 100
sales_tax_rate = 0.065
taxable = False
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sal_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sal_tax:.2f}")
    total = total + sal_tax
print(f"Total    : ${total:.2f}")
print("\n")
# Get the current date abd time.
now = dt.datetime.now()
# Make decision based on hour.
if now.hour < 12:
    print("Good morning")
else:
    print("Good afternoon")
print("I hope you are doing well")
# Statement with if elif and else.
print("\n")
light_color = "yellow"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
else:
    print("Proceed with caution")
print("This code executes no matter what")
print("\n")
# Repeating a Process with for.
# Looping through numbers in range.
for x in range(7):
    print(x)
print("All done")
print("\n")
for x in range(1, 10):
    print(x)
print("All done")
print("\n")
# Looping through a string.
for x in "snorkel":
    print(x)
print("Done")
print("\n")
my_word = "snorkel"
for x in my_word:
    print(x)
print("Done")
print("\n")
# Looping through a list.
for x in ["The", "rain", "in", "Spain"]:
    print(x)
print("Done")
print("\n")
# Bailing out of a loop.
ancwers = ["A", "C", "", "D"]
for answer in ancwers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done")
print("\n")
# Looping with continue.
ancwers = ["A", "C", "", "D"]
for answer in ancwers:
    if answer == "":
        print("Incomplete")
        continue
    print(answer)
print("Loop is done")
print("\n")
# Nesting loops.
# Outer loop
for outer in ["First", "Second", "Thid"]:
    print(outer)
    # inner loop
    for inner in range(3):
        print(inner + 1)
print("Both loops are done")
# Out of both loops
print("\n")
# Looping with while.
counter = 65
while counter < 91:
    print(str(counter) + " = " + chr(counter))
    counter += 1
print("All done")
print("\n")
# while and continue.
print("Odd numbers")
counter = 0
while counter < 10:
    # Get a random number
    number = random.randint(1, 999)
    if int(number/2) == number/2:
        # If it's an even number, don't print it
        continue
    # Otherwise, if it's odd, print it and increment the counter.
    print(number)
    counter += 1
print("Loop is done")
print("\n")
# while and break.
print("Numbers that areb't evenly divisible by five")
counter = 0
while counter < 10:
    # Get a random number
    number = random.randint(1, 999)
    if int(number/5) == number/5:
        # if it's evenly divisible by 5, bail out.
        break
    # Otherwise, print it and keep going for a while.
    print(number)
    counter += 1
print("Loop is done")
print("\n")

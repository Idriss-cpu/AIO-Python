import datetime as dt
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

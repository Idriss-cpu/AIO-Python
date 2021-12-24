# This is a Python comment in my first Python app
# This variable contains an integer
QUANTITY = 14
# This variable contains a float
UNITE_PRICE = 26.99
# This variable contains the result of multiplying quantity times unit price
EXTENDED_PRICE = QUANTITY * UNITE_PRICE
# Show the results
print(EXTENDED_PRICE)
X = -4
Y = abs(X)
print(X)
print(Y)
print(round(EXTENDED_PRICE, 3))
print(bin(Y))
# Test line
# date : 23/12/2021
# GETTING THE LENGTH OF A STRING
S1 = ""
S2 = " "
S3 = "A B C"
print(len(S1))
print(len(S2))
print(len(S3))
# Working with common string operators
S = "Abracadabra Hocus Pocus you're a Turtle dove"
print("t" in S)
print("T" in S)
print("T" not in S)
print("-" * 15)
print(S[0])
print(S[33:39])
print(S[0:44:3])
print(min(S))
print(max(S))
print(S.index("P"))
print(S.index("o", 22, 44))
print(S.count("a"))
# Working with ASCII
print(ord("A"))
print(chr(65))
# Manipulating strings with methods
S1 = "There is no such word as schmmedledorp"
S2 = "    a b c   "
S3 = "ABC"
print(S3.capitalize())
print(S1.count(" "))
print(S1.find("."))
print(S3.islower())
print(S3.lower())
print(S2.lstrip())
print(S1.swapcase())
print(S1.title())
print(S1.upper())
print(S2)
print("**** Dates and Times ***")

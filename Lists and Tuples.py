# Working with lists & tuples.
from tkinter.font import names


students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
# Is Anita in the list ?
has_anita = "Anita" in students
print(has_anita)

# Is Bob in the list ?
has_bob = "Bob" in students
print(has_bob)
print("\n")
# Getting length of list.
print(len(students))
print("\n")
# Adding an item to the end of a list.
# Add the name Goober to the list.
students.append("Goober")
new_student = "Amanda"
# Add whatever name is in new_student to the list.
students.append(new_student)
# Print The entire list.
print(students)
print("\n")
# Inserting an item into a list.
student_name = "Lupe"
# Add student_name to front of the list.
students.insert(0, student_name)
# Show me the new list.
print(students)
print("\n")
# Changing an item in a list.
students[3] = "Hobart"
print(students)
print("\n")
# Combining lists.
# Create two lists of names.
list1 = ["Zara", "Lupe", "Hong", "Alberto", "jake"]
list2 = ["Huey", "Dewey", "Louie", "Nader", "Bubba"]
# Add list2 names to list1.
list1.extend(list2)
print(list1)
print("\n")
# Removing list items.
letters = ["A", "B", "C", "D", "C", "E", "C"]
# Remove "C" from the list.
letters.remove("C")
print(letters)
print("\n")
# Remove itmes with pop().
# Make a Copy of first list item then remove it from list.
first_rmoved = letters.pop(0)
# Make a Copy of last list item then remove it from list.
last_removed = letters.pop()
# Show the new list.
print(letters)
# Show what's been removed.
print(first_rmoved + " and " + last_removed + " were removed from the list.")
print("\n")
# Counting how many times an item appears in a list.
# Create a list of strings.
grades = ["C", "B", "A", "D", "C", "B", "C"]
# Count the B's.
b_grads = grades.count("B")
# Use a variable for value to count.
look_for = "C"
c_grades = grades.count(look_for)
print("There are " + str(b_grads) + " B grades in the list.")
print("There are " + str(c_grades) + " " + look_for + " grades in the list.")
# Count F's too.
print("There are " + str(grades.count("F")) + " F grades in the list.")
print("\n")
# Find the index for B.
b_index = grades.index("B")
# Find the index for F.
look_for = "F"

# Show the results.
print("The first B is index " + str(b_index))
print("\n")

print("\n")
# See if the item is in the list.
if look_for in grades:
    # If it's in the list, get and show the index.
    print(str(look_for) + " is at index " + str(grades.index(look_for)))
else:
    # If not in the list, don't even try for index number.
    print(str(look_for) + " isn't in the list.")
# Create a list of strongs
Names = ["Zara", "Lupe", "Hong", "Alberto", "jake", "Tylor"]
# Create a list of numbers
Numbers =  [14, 0, 56, -4, 99, 56, 11.23]
# Sort the names list
Names.sort()
# Sort the numbers list
Numbers.sort()
# Show the results
print(Names)
print(Numbers)



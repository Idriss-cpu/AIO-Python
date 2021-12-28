# Working with lists & tuples.
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

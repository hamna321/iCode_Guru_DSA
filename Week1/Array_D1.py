subjects = ["Computer", "Maths", "Ps", "IS", "Ps"]

# Accessing the third element of the list
print(subjects[2])

# Length of the array
print(len(subjects))

# Printing all elements in the list
for subject in subjects:
    print(subject)

# Appending "Programming" to the list
subjects.append("Programming")
print(subjects)

# Removing an element ("Maths") from the array using remove()
subjects.remove("Maths")

print(subjects)

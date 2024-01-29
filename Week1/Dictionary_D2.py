# Elements in the Dictionary
Student = {
    "Name" : "Hamna",
    "Class" : 3,
    "Section" : "Red"
}
print(Student["Section"]) # print the specific element --> from the dictionary
# update the student dictionary
Student = {
   "Name" : "Hamna",
    "Class" : 3,
    "Section" : "Red",
    "Class" : 6 
}
print(Student["Class"])
# Removing the element from dict:
Student = {
    "Name": "Hamna",
    "Class": 3,
    "Section": "Red"
}
del Student["Name"]  # Use del keyword to delete the "Name" key from the dictionary
print(Student)

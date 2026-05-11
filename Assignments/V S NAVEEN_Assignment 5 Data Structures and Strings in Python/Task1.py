# Task 1: Create a Dictionary of Student Marks

# Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

# Ask the user to enter a student's name
name = input("Enter the student's name: ")

# Check if the student exists in the dictionary
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the dictionary.")
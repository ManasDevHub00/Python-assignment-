# Step 1: Create a dictionary of student marks
student_marks = {
    "Rahul": 85,
    "Anita": 92,
    "Manas": 88,
    "Riya": 76,
    "Amit": 90
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show message if not found
if name in student_marks:
    print("Marks of", name, ":", student_marks[name])
else:
    print("Student not found in the record.")
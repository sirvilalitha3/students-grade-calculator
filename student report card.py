# Student Report Card

print("===== STUDENT REPORT CARD =====")

# Get student details from the user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Create a list of subjects
subjects = [ "Maths", "statistics", "Data Science",]

# Create an empty dictionary to store subject marks
marks = {}

# Use for loop to get marks for each subject
for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))

    # Store the subject and its marks in the dictionary
    marks[subject] = mark


# Calculate the total marks
total = sum(marks.values())

# Calculate the average marks
average = total / len(subjects)


# Decide the grade based on average marks
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"


# Check whether the student passed or failed
if average >= 40:
    result = "PASS"
else:
    result = "FAIL"


# Display the final report card
print("\n===== REPORT CARD =====")

# Display student details
print("Student Name:", name)
print("Roll Number:", roll_no)

# Display marks of each subject
print("\nSubject Marks:")

# Loop through the dictionary and display each subject and mark
for subject, mark in marks.items():
    print(subject, ":", mark)

# Display total, average, grade and result
print("\nTotal Marks:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)


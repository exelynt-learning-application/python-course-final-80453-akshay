# student_grade.py

# Get student name
student_name = input("Enter student name: ")

# Get marks for 3 subjects
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

# Validate marks
if (mark1 < 0 or mark1 > 100 or
    mark2 < 0 or mark2 > 100 or
    mark3 < 0 or mark3 > 100):
    print("Invalid marks! Please enter marks between 0 and 100.")
else:
    # Calculate total and average
    total = mark1 + mark2 + mark3
    average = total / 3

    # Determine grade
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

    # Display results
    print("\n----- Student Result -----")
    print("Student Name :", student_name)
    print("Total Marks  :", total)
    print("Average      :", average)
    print("Grade        :", grade)

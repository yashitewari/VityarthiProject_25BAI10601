# VityarthiProject_25BAI10601
# Automatic Grade Calculator for n subjects

# 1. Input
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0.0

for i in range(1, n + 1):
    mark = float(input(f"Enter marks for Subject {i} (0-100): "))
    total += mark

# 2. Processing: calculate average (percentage)
average = total / n

# 3. Processing: decide grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# 4. Output
print("\n--- Result ---")
print("Student:", name)
print("Number of subjects:", n)
print("Total Marks:", total)
print("Average Percentage:", round(average, 2))
print("Grade:", grade)

# VityarthiProject_25BAI10601
Automatic Grade Calculator is a Python-based tool that helps teachers quickly compute student totals, percentages, and letter grades from raw marks, reducing manual effort and errors. It applies course concepts like input validation, modular design, algorithms, and testing to solve a real classroom need.

- Problem definition:
  
Teachers manually calculate totals, averages, and grades for each student, which is slow and error‑prone.
This program automatically calculates the average percentage and final grade from marks entered for any number of subjects.



- Requirement analysis

1. Input student name.

2. Input number of subjects.

3. Input marks for each of the subjects respectively.

4. Compute total and average percentage.

5. Assign a letter grade (A–F) based on the average.

6. Display the student’s name, number of subjects, total, average, and grade.

   

- Top-down design / modularization
  
~Main steps:

1. Read inputs (name, number of subjects, marks).

2. Process data (sum marks, compute average, decide grade).

3. Output a simple report.

~Logic is grouped into clear blocks (Input, Processing, Output) using comments.


- Algorithm development
 
Step 1: Start.

Step 2: Read name.

Step 3: Read integer n (number of subjects).

Step 4: Set total = 0.

Step 5: Repeat from i = 1 to n:

Step 6: Read mark for subject i.

Step 7: Add mark to total.

Step 8: Compute average = total / n.

Step 9: If average >= 90, grade = "A".
 
 Else if average >= 80, grade = "B".
 
 Else if average >= 70, grade = "C".
 
 Else if average >= 60, grade = "D".
 
 Else grade = "F".

Step 10: Print name, number of subjects, total, average, and grade.

Step 11: Stop.

- Implementation notes
1. Uses basic Python features: input(), int, float, for loop, arithmetic, and if‑elif‑else.

 
2. Works for any positive number of subjects because of the for i in range(1, n + 1) loop.

- Testing and refinement

1. Test with different values of n (e.g., 1, 3, 5).

 
2. Try high averages (e.g., 95) to check grade A and low ones (e.g., fifty‑sixty) to check other grades.

 
 
3. Test invalid inputs (like text instead of numbers) to see where future improvements (validation) could be added.

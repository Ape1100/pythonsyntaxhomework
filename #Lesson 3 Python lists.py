#Lesson 3 Python lists 
# Task 1: Grades in descending order
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print("Sorted grades in descending order:", sorted_grades)

# Task 2: Average grade
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

# Task 3: "Failed entries"
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"

print("Grades with 'Failed' replacement for grades below 80:", grades)

#2. Advanced List Methods and Identity Operators

# Task 1: Students who both submitted assignments and attended class
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_students = [student for student in submitted if student in attended]
print("Students who both submitted assignments and attended class:", common_students)

# Task 2: Studenst who attended and submitted assignemnts 
are_identical = sorted(submitted) == sorted(attended)
print("Are the two lists identical in terms of content?", are_identical)

# Task 3: Remove students from the attended list who did not submit their assignment
attended[:] = [student for student in attended if student in submitted]
print("Attended list after removing students who did not submit their assignment:", attended)

#3 Advance slicing 


#Given list of temperatures
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

#Task 1: Extract temperatures for the second week (7 days) of the month
second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week:", second_week_temperatures)
#Task 2: Extract all temperatures above 100
above_100_temperatures = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", above_100_temperatures)

#4 Deep dive into python lists 
#integrate lists to solve complex problems

# Given lists
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1: Filter out students with grades below 80
filtered_students = [(name, grade, activity) for name, grade, activity in zip(students, grades, activities) if grade < 80]
for student_info in filtered_students:
    print("Name: {}, Grade: {}, Activity: {}".format(*student_info))

# Task 2: Create a new list for approved students
students_approved = [name for name, grade in zip(students, grades) if grade >= 80]

# Task 3: Print the list of approved students
print("List of approved students:", students_approved)


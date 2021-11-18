student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_students = 0
total_height = 0

for height in student_heights:
  total_students += 1
  total_height += height

average_height = round(total_height / total_students)
print(f"The average height of these {total_students} students is {average_height}cm.")

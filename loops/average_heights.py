student_heights = input("Input a list of the student heights\n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(f"the height of the students: {student_heights}")

sum_heights = 0
student = 0
for height in student_heights:
    sum_heights += height
    student += 1

avg_height = sum_heights / student
print(f"the avg height of the student group is {avg_height}")
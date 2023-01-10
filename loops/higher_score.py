student_scores = input("Input a list of the student scores\n").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(f"the socore list of the students: {student_scores}")

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"the highest score of the student group is {highest_score}")
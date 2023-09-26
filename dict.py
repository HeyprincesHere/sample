student_scores = {
    "john": 85,
    "alice": 92,
    "michael": 78,
    "emma": 95,
    "daniel": 83
}
total_scores = 0
num_students = len(student_scores)

for score in student_scores.values():
    total_scores += score

average_score = total_scores / num_students
print("Average score:", average_score)

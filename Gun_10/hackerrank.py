n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

# The sum of the scores and the result divided by 3 for the average
print("%.2f" % (sum(student_marks[query_name])/3))
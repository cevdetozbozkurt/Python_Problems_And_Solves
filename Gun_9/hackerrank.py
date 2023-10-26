#list of students and scores
lst = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name,score])

# find the second lowest score

scores = set([lst2[1] for lst2 in lst])
secondLowest = sorted(scores)[1]

# Get the names of students with the second lowest score

names = [lst2[0] for lst2 in lst if lst2[1] == secondLowest]

names.sort()

for i in names:
    print(i)
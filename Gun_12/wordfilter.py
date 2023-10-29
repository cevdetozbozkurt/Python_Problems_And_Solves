words = ["cat", "car", "code", "home", "learn", "fun", "job", "love", "friend", "zoo", "enjoy", "happiness", "family", "goal", "desire"]

letter = str(input())

for i in words:
    for j in i:
        if letter == j:
            print(i)
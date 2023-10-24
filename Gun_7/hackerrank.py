x = input()
y = input()
z = input()
n = input()

coordinates = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                coordinates.append([i,j,k])

print(coordinates)
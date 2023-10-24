n = int(input())
arr = map(int, input().split())

if n in range(2,11):
    lst = []
    for i in arr:
        lst.append(i)
    lst.sort()
    lst.reverse()
    index = 0 
    while True:
        if lst[index] != lst[index+1]:
            print(lst[index+1])
            break
        elif lst[index] == lst[index+1]:
            index += 1
else:
    print("sorry we can't calculate it!!!")
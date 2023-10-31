ornek = "merhaba dunya"

lst = []
isIn = False
for i in range(len(ornek)):
    for j in range(len(ornek)):
        if ornek[i] != ornek[j]:
            isIn = True
        else:
            isIn = False
    if isIn:
        lst.append(ornek[i])
print(lst)
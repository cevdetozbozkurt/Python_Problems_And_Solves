print("ciksi yapmak icin 'q' ya basiniz...")

cikis = True

while cikis:
    a = input()
    if a == "q":
        cikis = False
    else :
        b = input()
    
    if int(a) in range(1,6) and int(b) in range(10,22):
        print("Acik (Open)")
    else:
        print("Kapali (Closed)")
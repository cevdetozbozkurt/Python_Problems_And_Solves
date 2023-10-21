def withdrawMoney(withdrawAmount, int(balance)):
    if(withdrawAmount >= balance):
        balance -= withdrawAmount
    else:
        print("Bakiyeniz yetersiz")

print("Cikis yapmak icin q ya basiniz...")

balance = 2000

q = True

while q:
    withdrawAmount = input("Cekmek istediginiz tutari giriniz")

    if withdrawAmount == "q":
        print("cikis yapiliyor...")
        q = False
    else if int(withdrawAmount) > 0:
        withdrawMoney(int(withdrawAmount),balance)
    else:
        print("Lutfen gecerli bir deger giriniz...")

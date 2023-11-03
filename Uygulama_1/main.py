from NotDefteri import NotDefteri

if __name__ == "__main__":
    notdefteriInstance = NotDefteri()
    while  notdefteriInstance.program:
        print("Yapabileceginiz Islemler ;")
        print("1. Not Ekle")
        print("2. Not Guncelle")
        print("3. Not Sil")
        print("4. Notlari Listle")
        print("5. Cikis")
        prompt = input("Lutfen bir islem seciniz (1/2/3/4/5) : ")
        print("")
        if prompt == "1":
            notdefteriInstance.NotEkle()
        elif prompt == "2":
            notdefteriInstance.NotGuncelle()
        elif prompt == "3":
            notdefteriInstance.NotSil()
        elif prompt == "4":
            notdefteriInstance.NotListele()
        elif prompt == "5":
            notdefteriInstance.program = notdefteriInstance.Cikis()
        else:
            print("Geçersiz bir seçim yaptiniz. Lütfen tekrar deneyin.")
            print("")
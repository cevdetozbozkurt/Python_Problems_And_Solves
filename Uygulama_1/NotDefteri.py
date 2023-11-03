class NotDefteri:
    
    def __init__(self):
        self.program = True
        self.Notlar = {}
    def NotEkle(self):
        baslik = input("Not basligini Giriniz : ")
        icerik = input("Not icerigini giriniz : ")
        self.Notlar[baslik] = icerik
        print(f"Not Eklendi {baslik}")
        print("")

    def NotGuncelle(self):
        baslik = input("Guncellenecek notun basligini giriniz: ")
        newContent = input("yeni icerigi giriniz: ")
        self.Notlar.update({f"{baslik}":f"{newContent}"})
        print(f"Not guncellendi: {baslik}")
        print("")

    def NotSil(self):
        baslik = input("Silinecek notun basligini giriniz: ")
        if baslik in self.Notlar.keys():
            self.Notlar.pop(baslik)
            print(f"Not silindi {baslik}")
        else:
            print("Silinecek notun basligi dogru degil lutfen tekrar ediniz...")
        
        print("")

    def NotListele(self):
        keys = self.Notlar.keys()
        print("Notlariniz : ")
        for i in keys:
            print(f"{i}: {self.Notlar[i]}")
        print("")
    def Cikis(self):
        print("Not Defteri uygulamasi kapatiliyor...")
        return False


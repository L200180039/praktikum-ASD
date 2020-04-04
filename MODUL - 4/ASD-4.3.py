class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTif("Jainal", 10, "Sukoharjo", 240000)
c1 = MhsTif("Fandit", 51, "Sragen", 230000)
c2 = MhsTif("Diko", 2, "Surakarta", 250000)
c3 = MhsTif("Ijul", 18, "Surakarta", 235000)
c4 = MhsTif("Ghani", 4, "Boyolali", 240000)
c5 = MhsTif("Rizki", 31, "Salatiga", 250000)
c6 = MhsTif("Bagus", 13, "Klaten", 245000)
c7 = MhsTif("Iqbal", 5, "Wonogiri", 245000)
c8 = MhsTif("Khalid", 23, "Klaten", 245000)
c9 = MhsTif("Azka", 64, "Karanganyar", 270000)
c10 = MhsTif("Bima", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
#NOMER 3
def uangSakuterkecil():
    a = Daftar[0].uangSaku
    x  =[]
    for i in range(len(Daftar)):
        if a> Daftar[i].uangSaku:
            a = Daftar[i].uangSaku
    for i in range(len(Daftar)):
        if Daftar[i].uangSaku == a:
            x.append(Daftar[i].nama)
    return x

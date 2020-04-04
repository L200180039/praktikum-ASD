class Manusia(object):
    """kelas 'manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print ("salam, namaku",self.nama)
    def makan(self,s):
        print("saya baru saja makan",s)
        self.keadaan = "kenyang"
    def olahraga (self,k):
        print("saya baru saja latihan",k)
        self.keadaan = 'lapar'
    def mengalikandengandua(self,n):
        return n*2

##p1 = Manusia("Fatimah")
##p1.ucapkansalam()

class Mahasiswa(Manusia):
    """class mahasiswa yang dibangun dari kelas manusia"""
    def __init__(self,nama,NIM,kota,us):
        """metode inisiasi ini menutupi metode inisiasi di kelas manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotatinggal =kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama +",NIM"+ str(self.NIM)\
            +",tinggaldi" + self.kotatinggal \
            +", uangsaku Rp" + str(self.uangsaku) \
            +"tiap bulannya"
        return s
    def ambilnama (self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambiluangsaku(self):
        return self.uangsaku
    def makan(self,s):
        """metode ini menutupi metode 'makan' nya classs manusia.
        mahasiswa kalau makan sambil belajar."""
        print("saya baru saja makan", s,"sambil belajar")
        self.keadaan = "kenyang"
        
m1 = Mahasiswa("Jamil",234,"surakarta",250000)
m2 = Mahasiswa("andi",365,"magelang",375000)
m3 = Mahasiswa ("Sri",676,"yogyakarta",240000)


class MhsTIF(Mahasiswa):
    """class MhsTIF yang dibangun dari class mahasiswa"""
    def katakanpy(self):
        print("python is cool")
        
c0 = MhsTIF("Ika",10,"Sukoharjo",240000)
c1 = MhsTIF("Budi",51,"Sragen",230000)
c2 = MhsTIF("Ahmad",2,"Surakarta",250000)
c3 = MhsTIF("Candra",18,"Surakarta",235000)
c4 = MhsTIF("Eka",4,"Boyolali",240000)
c5 = MhsTIF("Fandi",31,"Salatiga",250000)
c6 = MhsTIF("Deni",13,"Klaten",245000)
c7 = MhsTIF("Galuh",5,"Wonogiri",245000)
c8 = MhsTIF("Janto",23,"Klaten",245000)
c9 = MhsTIF("Hasan",64,"Karanganyar",270000)
c10 = MhsTIF("Khalid",29,"Purwodadi",265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

target = "Klaten"
for i in Daftar:
    if i.kotatinggal == target:
        print(i.nama + " tinggal di "+target)

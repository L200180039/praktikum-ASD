#3A
def jumlahHurufVokal(ch) :
    b = len(ch)
    a = 0
    for i in ch :
        if (i=='A' or i=='a' or i=='E' or i =='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
            a += 1
    return b,a

v = jumlahHurufVokal("Guntur")

print(v)

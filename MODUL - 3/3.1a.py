#1a
def cekMatrik(matrix):
    panjang = len(matrix)
    hasil = True
    for x in matrix:
        lebar = len(x)
        if lebar != panjang:
            hasil = False
            break

        for i in x:
            if type(i) != int:
                hasil = False
                break
    return hasil

m1 = [[2,3],[4,5]]
m2 = [[10,20],[5,6]]
m3 = [[4,8,3],[2,"8",4],[3,6,8]]
m4 = [[6,2,7],[2,8]]

print("m1 =", cekMatrik(m1))
print("m2 =", cekMatrik(m2))
print("m3 =", cekMatrik(m3))
print("m4 =", cekMatrik(m4))
            
#1b
def Ukuran(matrix):
    return ("Ukuran matrix = "+str(len(matrix))+" x "+str(len(matrix[0])))

m1 = [[2,3],[4,5]]
m2 = [[10,20],[5,6]]

print(Ukuran(m1))
print(Ukuran(m2))

#1c
a = [[1,2],[3,4]]
b = [[7,2],[1,4]]
c = [[1,"a","b"],[3,4,"c"]]
d = [[2,1],[3,4],[6,5]]
e = [[3,2,1],[5,4,3]]
f = [[1,2,3],[4,5,6],[1,5,6]]

def jumlah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("Ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("Ukuran beda")

jumlah(a,b)
jumlah(a,d)
     
#1d
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("Dapat Dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("Tidak memenuhi syarat")

zz = [[1,2,3],[1,2,3]]
zx = [[1],[2],[3]]
kali(zz,zx)
kali(a,b)
kali(a,e)
kali(a,zx)

#1e
def determHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "Tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "Tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total


z = [[4,2],[1,7]]
x = [[3,4,5],[1,3,2],[1,2,3]]
v = [[2,-3,0,0],[2,1,-5,2],[3,1,3,5],[6,7,-8,4]]
r = [[10,22,44,11,12],[2,2,1,1,9],[1,2,3,4,5],[5,2,5,3,8],[1,2,5,3,11]]
print(determHitung(z))
print(determHitung(x))
print(determHitung(v))
print(determHitung(r))
print(determHitung(d))
print(determHitung(e))

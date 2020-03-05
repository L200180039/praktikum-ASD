#2
def gambarlahPersegiEmpat(a,b) :
    for i in range(a) :
        if ((i+1) == 1) :
            print(b*"@")
        elif ((i+1) == a) :
            print(b*"@")
        else :
            print("@"+" "*(b-2)+"@")

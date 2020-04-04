def Binse(kumpulan,target):
    #mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1
    #secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low <= high :
        #temukan pertengahan runtut itu
        mid = (high + low) // 2
        #apakah pertengahan memuat target ?
        if kumpulan[mid] == target:
            return True
        #ataukah targetnya disebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
        #ataukah targetnya di sebelah kanannya ?
        else:
            low = mid + 1
    #jika runtutnya tidak bisa di belah lagi,berarti targetnya tidak ada
    return False

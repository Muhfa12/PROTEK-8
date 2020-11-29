# 8
buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
def rata2HargaBuah(buah):
    zigma = 0
    jumlah = 0    
    for x,y in buah.items():
        zigma += y
        jumlah += 1
    rata2 = zigma / jumlah
    return rata2
print("Rata - rata harga buah adalah : ", rata2HargaBuah(buah))

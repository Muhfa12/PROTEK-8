# 9
buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
def jumlahBuah():    
    jumlah = int(input("Berapa Kg : "))        
    print("-----------------------------")
    print("Total Harga : ", buah.get(namaBuah, 0) * jumlah)
print("Daftar Buah : ")
for x,y in buah.items():
    print("- ", x, ": ", y)
while True:
    namaBuah = input("Nama buah yang dibeli : ")    
    if(namaBuah not in buah.keys()):
        print("Maaf, buah yang anda masukkan tidak ada dalam data")
        continue
    else:
        while True:
            try:
                jumlahBuah()
                break            
            except ValueError:
                continue
        break

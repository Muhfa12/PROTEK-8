# 12
buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
def jumlahBuah(namaBuah):
    jumlah = int(input("Berapa Kg : ")) 
    harga = buah.get(namaBuah, 0) * jumlah
    return harga
def beliBuah(buahDict):
    print("Daftar Buah : ")
    for x,y in buahDict.items():
        print("- ", x, ": ", y)
    total = []
    lanjut = True  
    while(lanjut == True):   
        namaBuah = input("Nama buah yang dibeli : ").lower()
        if(namaBuah not in buahDict.keys()):
            print("Maaf, buah yang anda masukkan tidak ada dalam data")
            continue            
        else:
            try:
                harga = jumlahBuah(namaBuah)
                total.append(harga)  
                opsi = input("Beli buah yang lain (y/n) ? ").lower()
                if(opsi == "y"):
                    lanjut = True  
                elif(opsi == "n"):
                    lanjut = False
                else:
                    print("Input Tidak Valid")
                    break   
            except ValueError:
                    print("Input Tidak Valid, Silahkan Ulangi")
                    continue
    print("------------------------------")
    print("Total Harga : ", sum(total))
def tambahBuah(buahDict):
    namaBuahBaru = input("Masukkan nama buah : ").lower()
    while True:
        try: 
            if(namaBuahBaru in buahDict.keys()):
                print("Buah ", namaBuahBaru, "sudah ada di dalam data, Silahkan masukkan harga terbaru")
                hargaBuahBaru = int(input("Masukkan harga satuan : "))
                dictBuahBaru = {namaBuahBaru : hargaBuahBaru}
                buahDict.update(dictBuahBaru)
                print("Data Buah : ")
                for x,y in buahDict.items():
                    print("- ", x, "(harga : ", y, ")")
            else:
                hargaBuahBaru = int(input("Masukkan harga satuan : "))
                buah[namaBuahBaru] = hargaBuahBaru
                print("Data Buah : ")
                for x,y in buahDict.items():
                    print("- ", x, "(harga : ", y, ")")
            break
        except ValueError:
            print("Harga yang anda masukkan tidak valid")
            continue
def hapusBuah(buahDict):
    buahHapus = input("Masukkan nama buah yang ingin anda hapus : ").lower()
    if(buahHapus in buahDict.keys()):
        del buahDict[buahHapus]
        print("Buah ", buahHapus, "berhasil dihapus dari data")      
        print("Data Buah : ")
        for x,y in buahDict.items():
            print("- ", x, "(harga : ", y, ")")
    else :
        print("Buah yang anda maksud tidak ada dalam data, Silahkan coba lagi")
print("Menu : ")
print("A. Tambah data buah")
print("B. Beli buah")
print("C. Hapus data buah")
print("X. Keluar")
while True:
    pilihanMenu = input("Pilihan Menu : ").lower()
    if(pilihanMenu == "a"):
        tambahBuah(buah)
    elif(pilihanMenu == "b"):
        beliBuah(buah)
    elif(pilihanMenu == "c"):
        hapusBuah(buah)
    elif(pilihanMenu == "x"):
        break    
    else:
        print("Input Tidak Valid")
        continue

# 4
sayur = ["bayam", "kangkung", "wortel", "selada"]
def tambahSayur():
    sayurTambah = input("Masukkan nama sayur yang ingin anda tambahkan : ").lower()
    sayur.append(sayurTambah)
    return sayur
def hapusSayur():
    sayurHapus = input("Masukkan nama sayur yang ingin anda hapus : ").lower()
    if(sayurHapus in sayur):
        sayur.remove(sayurHapus)
    else:
        print("Sayur tersebut tidak ada dalam data")
    return sayur
def tampilkanSayur():
    print(sayur)
    
print("Apa yang bisa saya bantu : ")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")
print("X. Keluar")

while True:
    opsi = input("Pilihan Anda : ")
    if(opsi == "A" or opsi == "a"):
        tambahSayur()            
    elif(opsi == "B" or opsi == "b"):
        hapusSayur()
    elif(opsi == "C" or opsi == "c"):
        tampilkanSayur()
    elif(opsi == "X" or opsi == "x"):
        break    
    else :
        print("Input Tidak Valid")
        continue

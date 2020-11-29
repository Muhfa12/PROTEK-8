# 3
dataNama = []
a = True
while(a == True):
    nama = input("Masukkan Nama Mahasiswa : ")
    dataNama.append(nama)
    lanjut = input("Masukkan Nama Mahasiswa Lagi? (y/n) ")
    if(lanjut == "y"):
            a = True            
    elif(lanjut == "n"):
            a = False
    else:
        print("Input Tidak Valid")
        break
print()
dataNama.sort()
for b in range(len(dataNama)):
    print(dataNama[b], "(", len(dataNama[b]), "karakter )")

# 1
while True :
    try :
        n = int(input("Berapa banyak data yang anda inginkan? (Angka) : "))
        break
    except ValueError :
        print("Input Tidak Valid")
        continue
data = []
i = 0
while (i < n) :
    try :
        bil = int(input("Masukkan bilangan bulat yang anda inginkan : "))
        data.append(bil)
        i+= 1
    except ValueError :
        print("Input Tidak Valid")    
data.sort(reverse = True)
print(data)

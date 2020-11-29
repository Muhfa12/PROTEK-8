# 5
def kuadrat(bil):    
    bilSquare = []    
    for x in range(len(bil)):        
        a = bil[x] * bil[x]
        bilSquare.append(a) 
    return bilSquare
dataBil = [2, 4, 5, 6]
hasil = kuadrat(dataBil)
print(hasil)

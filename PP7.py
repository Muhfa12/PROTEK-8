# 7
buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
def termahal(dictionary):    
    key = list(dictionary.keys())
    values = tuple(dictionary.values())
    hargaTermahal = max(values)    
    indexHargaTermahal = values.index(hargaTermahal)
    print(key[indexHargaTermahal])
termahal(buah)

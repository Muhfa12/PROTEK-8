# 6
def sortStringByChar(data):   
    data.sort(reverse=True)
    return data
data = ["apel", "rambutan", "jeruk"]
dataSorted = sortStringByChar(data)
print("Data baru yang telah tersortir (descending) : ", dataSorted)

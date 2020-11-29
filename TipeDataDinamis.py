# 1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print(b)
print()

# 2
a.insert(3,10)
b.insert(2,15)
print(a)
print(b)
print()

# 3
a.append(4)
b.append(8)
print(a)
print(b)
print()

# 4
a.sort()
b.sort()
print(a)
print(b)
print()

# 5
c = a[0:8]
d = b[2:10]
print(c)
print(d)
print()

# 6
e = []
for i in range(len(c)) :
    element = c[i] + d[i]
    e.append(element)
    
print(e)
print()

# 7
dataTuple = tuple(e)

# 8
minTuple = min(dataTuple)
maksTuple = max(dataTuple)
sumTuple = sum(dataTuple)
print(minTuple)
print(maksTuple)
print(sumTuple)
print()

# 9
myString = "python adalah bahasa pemrograman yang menyenangkan"

# 10
charPenyusun = set(myString)
print(charPenyusun)
print()

# 11
listPenyusun = list(charPenyusun)
listPenyusun.sort()
print(listPenyusun)

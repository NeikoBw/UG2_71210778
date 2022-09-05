a1 = int(input("Masukkan Jumlah :"))
b1 = []
for i in range(0,a1):
    c = int(input("Masukan elemennya :"))
    b1.append(c)
a2 = int(input("Masukkan Jumlah :"))
b2 = []
for i in range(0,a2):
    c2 = int(input("Masukkan elemennya :"))
    b2.append(c2)

b1.extend(b2)
b1.sort()
print(b1)
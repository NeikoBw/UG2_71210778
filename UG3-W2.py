a1 = input("Masukkan kata ke-1 :")
a2 = input("Masukkan Kata ke-2 :")
set_1 = set()
set_2 = set()
for b1 in a1 :
    set_1.add(b1)
for b2 in a2 :
    set_2.add(b2)
print(set_1 & set_2)
# Nama file : import.py
# mengimport modul geometry2D

from matematika import geometry2D

# Persegi panjang
p = 10
l = 8

luas = geometry2D.luasPersegiPanjang(p, l)
kel = geometry2D.kelilingPersegiPanjang(p, l)

print("PERSEGI PANJANG")
print("Panjang\t:", p)
print("Lebar\t:", l)
print("Luas\t:", luas)
print("Keliling\t:", kel)

# Lingaran
jarijari = 3

luas = geometry2D.luasLingkaran(jarijari)
kel = geometry2D.kelilingLingkaran(jarijari)

print("\nLINGKARAN")
print("Jari-jari\t:", jarijari)
print("Luas\t:", luas)
print("Keliling\t:", kel)
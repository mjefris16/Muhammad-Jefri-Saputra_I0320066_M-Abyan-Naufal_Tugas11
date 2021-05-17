# Nama file : fromimport.py
# Mengimport fungsi luasPersegiPanjang

from matematika.geometry2D import luasPersegiPanjang

# Persegi panjang
p = 10
l = 8

luas = luasPersegiPanjang(p, l)

print("Persegi Panjang")
print("Panjang\t:", p)
print("Lebar\t:", l)
print("Luas\t:", luas)
# Nama file : geometry2D.py
import math

# Fungsi luas persegi panjang
def luasPersegiPanjang(p, l):
    return p * l

# Fungsi keliling persegi panjang
def kelilingPersegiPanjang(p, l):
    return 2 * (p+l)

# Fungsi luas bujur sangkar
def luasBujursangkar(s):
    return s*s

# Fungsi keliling bujur sangkar
def kelilingBujursangkar(s):
    return 4*s

# Fungsi luas lingkaran
def luasLingkaran(r):
    return math.pi * r * r

# Fungsi keliling lingkaran
def kelilingLingkaran(r):
    return 2 * math.pi * r

# Fungsi luas segitiga
def luasSegitiga(a, t):
    return (a*t)/2

# Fungsi keliling segitiga
def kelilingSegitiga(a, b, c):
    return a+b+c
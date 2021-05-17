# Nama file : paket.py
# Mengimport modul geometry2D
# yang berada didalam paket matematika
import matematika.geometry2D

def main():
    # Bujur sangkar
    sisi = 5

    luas = matematika.geometry2D.luasBujursangkar(sisi)

    print("BUJUR SANGKAR")
    print("Panjang sisi\t: ", sisi)
    print("Luas\t\t: ", luas)

if __name__ == '__main__':
    main()
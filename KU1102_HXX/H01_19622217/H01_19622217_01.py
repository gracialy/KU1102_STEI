# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 15 September 2022
# Deskripsi : Program memeriksa barang dengan keuntungan terbesar; input: harga dasar, harga jual; output: barang yang harus ditawarkan (keuntungan terbesar)

# KAMUS
# hargaDasarA, hargaDasarB, hargaDasarC : integer 
# hargaJualA, hargaJualB, hargaJualC    : integer
# untungA, untungB, untungC             : integer
# tawaran                               : string

# ALGORITMA
# Input
hargaDasarA=int(input("Masukkan harga dasar barang A: "))
hargaJualA=int(input("Masukkan harga jual barang A: "))
hargaDasarB=int(input("Masukkan harga dasar barang B: "))
hargaJualB=int(input("Masukkan harga jual barang B: "))
hargaDasarC=int(input("Masukkan harga dasar barang C: "))
hargaJualC=int(input("Masukkan harga jual barang C: "))

# untung = harga jual - harga dasar
untungA=hargaJualA-hargaDasarA
untungB=hargaJualB-hargaDasarB
untungC=hargaJualC-hargaDasarC

# Percabangan
# catatan: asumsi tidak ada keuntungan yang sama
if(untungA>untungB and untungA>untungC):
    tawaran="A"
elif(untungB>untungA and untungB>untungC):
    tawaran="B"
elif(untungC>untungA and untungC>untungB):
    tawaran="C"

# Output
print("Barang yang harus ditawarkan adalah barang", tawaran)
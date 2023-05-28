# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 9 November 2022
# Deskripsi : Program menghilangkan setiap elemen baris ke-i dan setiap elemen kolom ke-j dari suatu matriks; input: ukuran matriks awal, i baris yang dihilangkan, j kolom yang dihilangkan; output: matriks setelah penghilangan

# KAMUS
# kol, bar, hilangBar, hilangKol: int
# mtx: matriks of int
# i, j: int

# ALGORITMA PROGRAM UTAMA
kol=int(input("Masukkan M: ")) # kol
bar=int(input("Masukkan N: ")) # bar
# inisiasi matriks
mtx=[[0 for i in range (kol)] for j in range (bar)]

hilangBar=int(input("Masukkan i: ")) # i input
hilangKol=int(input("Masukkan j: ")) # j input

# input nilai matriks
for i in range (bar):
    for j in range (kol):
        mtx[i][j]=int(input(f"Masukkan elemen baris {i+1} kolom {j+1}: "))

# penghilangan
for i in range (1,bar+1):
    for j in range (1,kol+1):
        # jika baris dan kolom tidak termasuk elemen yang dihilangkan
        if (i!=hilangBar and j!=hilangKol):
            # debugging station
            # print(mtx[i-1][j-1], i, j)
            print(mtx[i-1][j-1], end=" ")
        # else: 
            #(i==hilangBar or j==hilangKol) elemen dihilangkan
    # tidak perlu enter jika tidak ada yang di-print dalam baris tersebut
    if (i!=hilangBar and j!=hilangKol):
        print()
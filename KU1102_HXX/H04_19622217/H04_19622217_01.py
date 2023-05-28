# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 1 November 2022
# Deskripsi : Program memeriksa nilai paling berat dari sebuah tumpukan berada di posisi paling bawah; input: tinggi tumpukan, banyak tumpukan, nilai-nilai benda dalam tumpukan; output: tumpukan memenuhi syarat atau tidak

# KAMUS
# matrix: matriks of int
# m, n: int (banyak baris & kolom matrix)
# i, j: int (indeks)
# heaviest: bool
# ans: str
# mtx: str

# ALGORITMA
m=int(input("Masukkan tinggi tumpukan: "))
n=int(input("Masukkan banyak tumpukan: "))

# inisiasi matriks
matrix=[[0 for i in range (n)] for j in range (m)]

# masukkan nilai matriks
print("Masukan susunan berat benda:")
# perulangan input tiap baris sebanyak m baris
for i in range (m):
    mtx=input() # masukan nilai dalam satu baris, setiap kolom dipisahkan oleh spasi
    # perulangan memisah nilai setiap kolom sebanyak n kolom
    for j in range (n):
        # masukan dipisah kolomnya dengan split()
        matrix[i][j]=int(mtx.split()[j])

# debugging station
print(matrix)

# pengecekan berat tumpukan
heaviest=True # tumpukan memenuhi syarat nilai paling bawah adalah nilai terberat
for i in range (n): # perulangan kolom
    for j in range (m-1): # perulangan baris
        # debugging station
        # print(matrix[m-1][i], "compare", matrix[j][i])
        # percabangan mengecek nilai baris terakhir dalam suatu kolom lebih kecil dari nilai(-nilai) di atasnya
        # tidak memenuhi syarat tumpukan
        if matrix[m-1][i] < matrix[j][i]:
            heaviest=False
        # else:
            # (matrix[m-1][i]>=matrix[j][i])
            # nilai baris terakhir dalam suatu kolom tidak lebih kecil dari nilai(-nilai) di atasnya
            # tumpukan masih memenuhi syaat

# kombinasi output
ans="Susunan tersebut "
if heaviest==True:
    ans+="memenuhi "
else: # heaviest==False
    ans+="tidak memenuhi "
ans+="perintah Tuan Leo."
print(ans)

# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 1 November 2022
# Deskripsi : Program menjumlahkan tinggi bangunan dalam sekolom yang lebih tinggi daripada gedung tertinggi yang pernah dijumpai dalam kolom itu; input: besar kota Kompeng, tinggi bangunan pada baris dan kolom; output: total tinggi terbesar dihitung dari atas atau bawah kolom

# KAMUS
# size: int (banyak baris & kolom city, banyak kolom map)
# city: array of int
# map: array of int
# i, j: int (indeks)
# mtx: str
# compare, save: int
# ans: int

# ALGORITMA
size=int(input("Masukkan besar Kota Kompeng: "))

# inisiasi matriks
city=[[0 for i in range (size)] for j in range (size)] # matriks memetakan tinggi
map=[[0 for i in range (size)] for j in range (2)] # matriks memetakan total tinggi dari atas dan bawah pada setiap kolom

# masukkan nilai matriks
# perulangan input tiap baris sebanyak size baris
for i in range (size):
    mtx=input() # masukan nilai dalam satu baris, setiap kolom dipisahkan oleh spasi
    # perulangan memisah nilai setiap kolom sebanyak size kolom
    for j in range (size):
        # masukan dipisah kolomnya dengan split()
        # masukkan hasil split anggota input ke-(j-1) ke dalam array
        city[i][j]=int(mtx.split()[j])

# debugging station
# print(city)
    
# menghitung nilai total
# atas ke bawah
for i in range (size): # perulangan kolom
    compare=city[0][i] # patokan tinggi sementara
    save=compare # total tinggi sementara
    # debugging station
    # print(f"[{i}], {compare}")
    for j in range (1, size): # perulangan baris
        # debugging station
        # print("with", city[j][i])
        if (compare<city[j][i]):
            compare=city[j][i]
            save+=compare
            # debugging station
            # print("new",compare, save)
        # else:
            # (compare>=city[j][i]): gedung yang tidak lebih tinggi tidak dihitung, patokan gedung tertinggi masih benar
    map[0][i]=save # mengisi matriks pemetaan total tinggi baris ke-1 kolom ke-(i+1)

# debugging station
# print(map)

# bawah ke atas
# perulangan yang sama seperti dari atas ke bawah namun patokan di baris terakhir dan perulangan baris menuju ke atas
for i in range (size): # perulangan kolom
    compare=city[size-1][i]
    save=compare
    # debugging station
    # print(f"[{i}], {compare}")
    for j in range (size-2, -1, -1): # perulangan baris
        # debugging station
        # print("with", city[j][i])
        if (compare<city[j][i]):
            compare=city[j][i]
            save+=compare
            # debugging station
            # print("new",compare, save)
    map[1][i]=save

# debugging station
# print(map)

# mencari total tertinggi
ans=0 # menyimpan total terbesar sementara
for i in range (2): # perulangan baris
    for j in range (size): # perulangan kolom
        # debugging station
        # print(f"baris {i} kolom {j}")
        if (map[i][j]>ans):
            ans=map[i][j]
        # else:
            # (map[i][j]<=ans): belum ada total yang lebih besar, jawaban masih benar

print("Foto terbaik memiliki total tinggi:", ans)


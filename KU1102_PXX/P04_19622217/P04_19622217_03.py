# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 9 November 2022
# Deskripsi : Program memeriksa keamanan raja dari kemungkinan gerak seluruh kuda; input: ukuran papan catur, posisi bidak-bidak; output: keamanan raja dari gerakan kuda

# KAMUS
# m: int
# papan: matriks of str
# safe: matriks of bool
# i, j: int
# rCoor: array of int

def kMove(kBar,kKol):
    # gerak kuda (berbentuk L)
    
    # KAMUS LOKAL
    # move: matriks of int
    # i: int

    # perubahan baris dan kolom dari semua kemungkinan gerakan
    # ada 2 jenis gerakan untuk setiap arah sesuai jarum jam
    # karena gerakan kuda yang kita gunakan diurai menjadi horizontal dan vertikal,
    # hanya ada 4 arah yaitu
    # kanan: 2 kanan 1 bawah, 1 kanan 2 bawah
    # bawah: 2 bawah 1 kiri, 1 bawah 2 kiri
    # kiri: 2 kiri 1 atas, 1 kiri 2 atas
    # atas: 2 atas 1 kanan, 1 atas 2 kanan
    move=[[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]

    # perulangan untuk setiap kemungkinan gerakan kuda
    for i in range (len(move)):
        # apakah ada cukup tempat untuk menggerakkan kuda?
        # (apakah menggerakkan kuda akan mengeluarkan kuda dari papan?)
        if(0<=(move[i][0]+kBar)<m and 0<=(move[i][1]+kKol)<m):
            safe[move[i][0]+kBar][move[i][1]+kKol]=False # tempat tersebut tidak aman
        # else:
            # kuda akan keluar papan jika digerakkan, gerakan ini tidak boleh dilakukan

# ALGORITMA PROGRAM UTAMA
m=int(input("Masukkan nilai m: ")) # ukuran catur

# inisiasi matriks
papan=[["" for i in range (m)] for j in range (m)]
# isi matriks
for i in range (m):
    for j in range (m):
        papan[i][j]=input(f"Masukkan elemen matriks ke-{i+1} {j+1}: ")
        if papan[i][j]=="R": # menemukan raja
            rCoor = [i,j]

# print matriks
print("Hasil papan catur")
for i in range (m):
    for j in range (m):
        print(papan[i][j], end=" ")
    print()

# menemukan kuda
safe=[[True for i in range (m)] for j in range (m)] # matriks posisi yang aman dari kuda
for i in range (m):
    for j in range (m):
        if papan[i][j]=="K":
            kMove(i,j)

# debugging station
'''print("safe")
for i in range (m):
    for j in range (m):
        print(safe[i][j], end=" ")
    print()'''

# cek posisi R
# jika koordinat kuda aman (bernilai True pada matriks safe)
if (safe[rCoor[0]][rCoor[1]]):
    print("Raja aman dari serangan kuda")
else: # not safe[rCoor[0]][rCoor[1]] (koordinat kuda tidak aman)
    print("Raja tidak aman dari serangan kuda")


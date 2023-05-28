# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 19 Oktober 2022
# Deskripsi : Program permainan lampu; input: jumlah lampu, frekuensi tombol ditekan, tombol yang ditekan; output: kondisi akhir lampu

# KAMUS
# n, times, change: int
# i, j: int
# kondisiLampu: array [0..n-1] of int

# ALGORITMA
n=int(input("Masukkan banyak lampu: "))
times=int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))

# menginisiasi array kondisiLampu berukuran n
# asumsi kondisi awal lampu mati
kondisiLampu=[0 for i in range (n)]

# meminta input tombol yang ditekan sebanyak times kali
for i in range (times):
    change=int(input("Tombol yang ditekan ke "+str(i+1)+": "))
    # lampu yang berubah kondisi adalah
    # - lampu yang ditekan tombolnya (indeks=change-1)
    # - lampu sebelah kiri (indeks=change-1-1=change-2)
    # - lampu sebelah kanan (indeks=change-1+1=change)
    for j in range (change-2,change+1):
        # jika range memenuhi jangkauan indeks (ada lampu di kiri atau kanan)
        if (0<=j<n):
            # lampu mati (0) akan jadi hidup (1) dan sebaliknya
            if (kondisiLampu[j]==0):
                kondisiLampu[j]=1
            else: # kondisiLampu [j]==1
                kondisiLampu[j]=0
        # else: tidak ada lampu di kiri atau kanan, tidak terjadi apa-apa

print("Keadaan akhir rangkaian lampu adalah", end=" ")

# print elemen dari array kondisiLampu dari kiri ke kanan
for i in range (n):
    print(kondisiLampu[i], end="")

print(".")
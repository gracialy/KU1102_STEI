# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : November 2022
# Deskripsi : Program mengalikan setiap digit suatu bilangan sampai tersisa bilangan 1 digit; input: bilangan; output: proses perkalian hingga tersisa 1 digit

# KAMUS
# mtx: matriks of int
# m, n: int (brs & kol mtx)

# ALGORITMA PROGRAM UTAMA
m=int(input("Masukkan nilai m: ")) # baris
n=int(input("Masukkan nilai n: ")) # kolom

# inisiasi matriks
mtx=[[0 for i in range (n)] for i in range (m)]

# matriks ular
'''now=1
for i in range (m):
    if (i%2==0):
        for j in range (n):
            mtx[i][j]=now
            now+=1
    else: # (i%2!=0)
        for j in range (n-1,-1,-1):
            mtx[i][j]=now
            now+=1'''

now=1
for j in range (n):
    mtx[0][j]=now
    now+=1
for i in range (1,m):
    mtx[i][n]=now
    now+=1


for i in range (m):
    if (i%2==0):
        for j in range (n):
            mtx[i][j]=now
            now+=1
    else: # (i%2!=0)
        for j in range (n-1,-1,-1):
            mtx[i][j]=now
            now+=1

print("Matriks spiral adalah:")
for i in range (n):
    for j in range (m):
        print(mtx[i][j], end=" ")
    print()
        
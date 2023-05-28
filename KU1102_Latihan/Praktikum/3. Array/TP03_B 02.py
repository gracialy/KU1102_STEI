# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 19 Oktober 2022
# Deskripsi : Program memeriksaAngkaSama

# KAMUS
# n, i , j: int
# sama: bool
# arr: array [0..n-1] of int

# ALGORITMA
n=int(input("Masukkan N: "))

arr=[0 for i in range (n)]

for i in range (n):
    arr[i]=int(input("Masukkkan bilangan ke "+ str(i+1)+": "))

sama=False

# memeriksa sampai indeks n-2, 
# karena indeks n-1 tidak ada lagi pembanding indeks setelahnya
for i in range (n-1):
    j=i+1 # mulai periksa dari indeks setelah i sampai indeks n-1
    while (j<n and sama==False):
        if (arr[i]==arr[j]):
            sama=True
            # jika sudah ditemukan yang sama, program berhenti memeriksa
        j+=1

# debugging station
# print(i, j)

if (sama):
    print("Tidak berbeda semua")
else:
    print("Berbeda semua")
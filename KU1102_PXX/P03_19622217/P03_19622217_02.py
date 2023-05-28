# NIM/Nama: 19622217/Lydia Gracia
# Tanggal: 26 Oktober 2022
# Deskripsi: Program mencari nilai terbesar ke-N; input: banyak data, N (nilai terbesar ke-), nilai data; output: nilai terbesar ke-N dari data

# KAMUS
# num, maxOrder, temp: int
# i, j: int
# arr: array [0..num-1] of int

# ALGORITMA
num=int(input("Masukkan banyak data: "))
maxOrder=int(input("masukkan nilai ke N: ")) # nilai terbesar ke-N

# inisiasi array untuk nilai data
arr=[0 for i in range (num)]
# pengisian nilai data ke dalam array
for i in range (num):
    arr[i]=int(input(f"Masukkan data ke-{i+1}: "))

# mengurutkan array dari paling kecil ke paling besar
for i in range (num):
    for j in range (i+1, num, 1):
        if (arr[j]<arr[i]):
            # swap
            # data yang lebih kecil index-nya akan dimajukan
            temp=arr[i] # variabel untuk menyimpan sementara salah satu nilai
            arr[i]=arr[j]
            arr[j]=temp
        # else: 
            # (arr[j]>=arr[i]), urutan sudah benar, tidak perlu ditukar

# debugging station
# print(arr)

# mencari nilai terbesar ke-N
# indeks diambil dari belakang (indeks negatif)
print(f"Nilai terbesar ke-{maxOrder} adalah {arr[-maxOrder]}")
# NIM/Nama: 19622217/Lydia Gracia
# Tanggal: 26 Oktober 2022
# Deskripsi: Program membandingkan uang yang didapat dari kota-kota yang dilewati; input: banyak kota, perubahan uang di setiap kota; output: jalur dengan perolehan uang terbesar

# KAMUS
# n, finish: int
# sum, sumRaw, sumNow: int
# max, idxMax: int
# i, j: int
# arr: array [0..n-1] of int
# store: array [0..n-1] of int
# fin: array [0..n-1] of int

# ALGORITMA
n=int(input("Masukkan banyak kota: "))
# inisiasi array sesuai banyak kota
arr=[0 for i in range (n)]
# memasukkan data perubahan uang pada array
for i in range (n):
    arr[i]=int(input(f"Masukkan perubahan uang di kota {i+1}: "))

# menyimpan kemungkinan uang terbesar dari suatu start
store=[0 for i in range (n)]
# menyimpan kota finish dari setiap data yang memenuhi syarat store
fin=[0 for i in range (n)]

# setelah start, tidak boleh ada kota yang dilompat sampai finish
# kota start: kota-(i+1)
for i in range (n):
    # inisiasi kota finish
    finish=i+1
    # jumlah uang dari banyak kota minimal yang harus dilewati (1 kota, start=finish)
    sumRaw=arr[i]
    # jumlah uang dari kemungkinan lain
    sumNow=sumRaw
    # inisiasi jumlah uang yang akan terbesar yang mungkin dari suatu start
    sum=sumRaw
    
    # debugging station
    # print(f"Start: {i+1}, Uang start: {sumRaw}")


    # memeriksa jumlah uang dari kota tersisa yang dapat dilewati
    for j in range (i+1, n, 1):
        sumNow+=arr[j]
        # jika ditemukan kemungkinan dengan jumlah uang lebih besar, update profil
        if (sum<sumNow):
            finish=j+1 # update kota finish
            sum=sumNow # update kemungkinan uang terbesar
            
            # debugging station
            # print(f"- Kota finish: {finish}, Jumlah uang: {sum}")
        # else:
            # (sum>=sumNow), data tidak perlu di-update
    
    # setelah sampai pada kemungkinan finish terakhir dari suatu start
    if (j==n-1):
        store[i]=sum
        fin[i]=finish
    # else:
        # (j<=n-1), data tidak perlu dipindahkan ke-array karena belum selesai dicek

# membandingkan jumlah uang terbesar dari masing-masing start
max=store[0]
idxMax=0
for i in range (1, n-1, 1):
    if (max<store[i]):
        max=store[i]
        idxMax=i
    # else:
        # (max>=store[i]), uang yang sudah disimpan tidak lebih kecil dari temuan baru
        # tidak perlu di-update

# debugging station
# print(f"Array uang: {store}")
# print(f"Array finish: {fin}")
# print(f"Indeks max: {idxMax}")
# print(f"Uang max: {max}, Kota awal: {idxMax+1}, Kota akhir: {fin[idxMax]}")

print(f"Tuan Kil dapat memiliki uang maksimum sebesar {max} dengan berawal pada kota {idxMax+1} dan berakhir di kota {fin[idxMax]}.")
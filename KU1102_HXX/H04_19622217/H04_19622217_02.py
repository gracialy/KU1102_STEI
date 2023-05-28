# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 1 November 2022
# Deskripsi : Program mengubah nilai pada array sampai menjadi nilai nol semua dengan mengurangkan dengan nilai minimal bukann 0; input: banyak nilai, nilai; output: langkah-langkah pada tiap pengoperasian hingga kondisi akhir dipenuhi

# KAMUS
# n: int
# arr: array [0..n-1] of int
# i: int
# isZero: bool
# minimal: int

# catatan: dalam fungsi def, saya tidak memasukkan array menjadi parameter mengingat saran pada modul

def min(k, mini):
    # mencari nilai minimal yang tidak 0

    # KAMUS LOKAL
    # i: int
    # initiate: bool
    # k, mini: int

    # ALGORITMA
    initiate=False # inisiasi nilai minimal belum ditemukan
    i=0
    # perulangan mengecek nilai minimal
    while (i<k):
        if (arr[i]!=0): # anggota yang dipertimbangkan adalah anggota bukan 0
            if (initiate==False):
                initiate=True
                mini=arr[i]
            else: # (initiate==True): sudah pernah ditemukan nilai bukan 0 yang menjadi nilai minimal sementara
                if (arr[i]<mini):
                    mini=arr[i]
                # else:
                    # (arr[i]>=minimal): nilai minimal sementara masih benar
        # else:
            #(arr[i]==0): anggota bernilai 0 tidak dipertimbangkan
        i+=1
    return mini

def zero(k, conZero):
    # mengecek apakah semua anggota array bernilai 0
    
    # KAMUS LOKAL
    # i: int
    # k: int
    # conZero: bool

    # ALGORITMA
    conZero=True
    for i in range (k):
        if (arr[i]!=0):
            conZero=False# ada anggota bukan 0
        # else: (arr[i]==0) kondisi semua 0 masih terpenuhi
    return conZero

# ALGORITMA PROGRAM UTAMA
n=int(input("Masukkan banyak nilai: "))

# inisiasi array
arr=[0 for i in range (n)]

# input nilai array
# asumsi setiap nilai awal array >=0
for i in range (n):
    arr[i]=int(input(f"Masukkan nilai ke-{i+1}: "))

# print array
isZero=False # inisiasi array awal memiliki anggota bukan 0
minimal=0 # inisiasi nilai minimal array awal untuk print keadaan pertama
while (isZero==False):
    for i in range (n):
        if (arr[i]!=0):
            arr[i]-=minimal
        # else:
            # (arr[i]==0): tidak dilakukan modifikasi pada anggota array 0
        print(arr[i], end=" ")
    print()
    isZero=zero(n, isZero) # cek ulang apakah semua anggota array 0 setelah modifikasi
    minimal=min(n, minimal) # cek ulang nilai minimal array setelah modifikasi
    
    # debugging station
    # print(isZero, minimal)
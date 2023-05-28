# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 9 November 2022
# Deskripsi : Program memeriksa banyak cara pemilihan sejumlah mahasiswa dari beberapa mahasiswa; input: jumlah mahasiswa, jumlah yang dipilih; output: banyak cara memilih mahasiswa

# KAMUS
# n, k: int

def factorial(x):
    # fungsi mencari nilai faktorial x!

    # KAMUS LOKAL
    # sum: int

    # debugging station
    # print("factorial", x)

    if x==0:
        return 1
    else: # asumsi x>0
        sum=1
        # perulangan perkalian sampai mencapai x
        for i in range (1,x+1):
            sum*=i
            # debugging station
            # print(i, sum)
        return sum

# ALGORITMA PROGRAM UTAMA
n=int(input("Masukkan N: ")) # banyak mahasiswa
k=int(input("Masukkan nilai K: ")) # banyak terpilih

# debugging station
# print(factorial (n))
# print(factorial(n-k), "*", factorial(k))

# C(n,k)=n!/((n-k)!*k!)
print(f"Tuan Riz memiliki {factorial (n)//(factorial(n-k)*factorial(k))} cara untuk memilih mahasiswa")
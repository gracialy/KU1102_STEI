# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 19 Oktober 2022
# Deskripsi : Program prosesMembalikkanKata

# KAMUS
# n, i, j: int
# str: str
# reverseStr: array [0..n-1] of str

# ALGORITMA
n=int(input("Masukkan N: "))
str=input("Masukkan kata: ")

# idea
# print(str[1])
# print(str[2], reverseStr[1], sep="")
# ...

# perulangan print kata sebanyak i karakter
for i in range (1,n+1):
    # untuk kata sebanyak i karakter, 
    # print dimulai dari indeks i-1 sampai indeks 0
    for j in range (i-1,-1,-1):
        print(str[j], end="")
    print()

# OR

reverseStr=[str[i] for i in range (-1,-n-1, -1)]

# idea
# print(reverseStr[-1])
# print(reverseStr[-2], reverseStr[-1], sep="")
# ...

for i in range (1,n+1):
    for j in range (-i,0,1):
        print(reverseStr[j], end="")
    print()
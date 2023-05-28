# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 7 November 2022
# Deskripsi : Program sumSequence

# KAMUS
# m: array of str
# n: int (brs & kol m)
# r1, r2, c1, c2: int
# sum: int

# ALGORITMA
n=int(input("Masukkan nilai N: "))
print("Masukkan matriks: ")
m=[input().split(" ", n-1) for i in range (n)]

# debugging station
# print(m)

r1=int(input("Masukkan nilai r1: "))
c1=int(input("Masukkan nilai c1: "))
r2=int(input("Masukkan nilai r2: "))
c2=int(input("Masukkan nilai c2: "))

# interval in box state
sum=0
for i in range (r1-1,r2):
    for j in range (c1-1,c2):
        # debugging station
        # print("check", m[i][j])
        if int(m[i][j])>0:
            sum+=int(m[i][j])

print(f"Jumlah yang didapat adalah {sum}.")
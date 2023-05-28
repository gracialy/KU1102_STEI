# 1
# Program perkalianKonstanta

# KAMUS
# m: matriks of int
# nBrs, mKol=int (ukuran baris dan kolom m)
# i, j: int (indeks)
# x: int (konstanta)

# ALGORITMA
'''nBrs=3; mKol=3
m=[ [1,2,3],
    [4,5,6],
    [7,8,9]]

x=int(input("x: "))

for i in range (nBrs):
    for j in range (mKol):
        m[i][j]*=x
        print(m[i][j], end=" ")
    print()'''

# 2
# Program transpose

# KAMUS
# matriks: matriks of int
# mTranspose: matriks of int
# n, m: int # ukuran baris dan kolom matriks
# m, n: int # ukuran baris dan kolom mTranspose
# i, j: int (indeks)

# ALGORITMA
'''n=2; m=3
matriks=[ [1,2,3],
    [4,5,6]]

# transpose
temp=n
n=m; m=temp
# inisiasi mTranspose
mTranspose=[[0 for j in range (m)] for i in range (n)]

# isi mTranspose
for i in range (n):
    for j in range (m):
        mTranspose[i][j]=matriks[j][i]
        print(mTranspose[i][j], end=" ")
    print()'''
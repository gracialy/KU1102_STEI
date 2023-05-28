# 2.3.1
# Program 10^x < N

# KAMUS
# n, x: int

# ALGORITMA
n=int(input("Masukkan N: ")) # asumsi n int

x=0

# perulangan menguji 10 pangkat x terhadap n
while (10**x <= n):
    x += 1 # kondisi akhir 10 pangkat x dipastikan lebih besar dari n

print(10**x)
'''

'''
# 2.3.2
# Program PolaSegitiga

# KAMUS
# n, i, j: int

# ALGORITMA
n=int(input("Masukkan n: ")) # asumsi n>0

# loop print pola sebanyak n baris
for i in range (1, n+1):
    # loop print angka berurutan sebanyak i kali dalam satu baris
    for j in range (1,i+1):
        print(j, end=" ")
    print()

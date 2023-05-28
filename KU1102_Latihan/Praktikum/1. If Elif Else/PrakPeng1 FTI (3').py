# 03 v.soal2
# mobil karya wisata

# mobil
# P
# E+G / E
# N+N / N+G
# G+G / -

# KAMUS
# p, e, n, g: int
# mobil=int

# INPUT
p=int(input("Masukkan banyak kelompok P: "))
e=int(input("Masukkan banyak kelompok E: "))
n=int(input("Masukkan banyak kelompok N: "))
g=int(input("Masukkan banyak kelompok G: "))

# ALGORITMA
mobil=p
print(mobil)

# n didahulukan karena wajib (n+n) atau (n+g)
if (n%2==0):
    mobil += (n//2) # agar mobil tetap integer, pastikan (n/2) bilangan bulat dengan floor
else: # (n%2!=0)
    if (g>=1):
        mobil += ((n//2)+1)
        g -= 1
print(mobil)

if (g>=e):
    mobil += e
    g -= e
    print(f"sisa g setelah e: {e}")
else: # (g<e)
    mobil += e
    g = 0
print(mobil)

if (g>=2):
    mobil += (g//2)
print(mobil)

# OUTPUT
print(f"Banyak mobil yang dibutuhkan adalah {mobil}")
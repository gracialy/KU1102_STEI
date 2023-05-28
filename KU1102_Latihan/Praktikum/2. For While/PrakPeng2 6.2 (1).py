# STAT: CLEAR
# Program BilanganAcak
# Formula: x(n)=(a*x(n-1)+b) mod m

# KAMUS
# x,a,b,m,n: int

# AlGORITMA
x=int(input("Masukkan nilai X0: ")) # nilai x0
a=int(input("Masukkan nilai A: "))
b=int(input("Masukkan nilai B: "))
m=int(input("Masukkan nilai M: "))
n=int(input("Masukkan nilai n: ")) # asumsi n>=0

# perulangan melakukan formula sebanyak n kali (mulai dari indeks 1)
for i in range (1,n+1):
    x=(a*x+b)%m # perbarui nilai x(n)

print("Nilai akhir yang didapat adalah", str(x) + ".")
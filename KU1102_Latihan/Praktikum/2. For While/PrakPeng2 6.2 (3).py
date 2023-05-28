# STAT: CLEAR
'''uuu i see'''
# Program PolaSegiempat

# AlGORITMA
a=int(input("Masukkan nilai A: ")) # selisih dengan kiri
b=int(input("Masukkan nilai B: ")) # selisih dengan atas
t=int(input("Masukkan tinggi segiempat: "))
l=int(input("Masukkan lebar segiempat: "))

# indeks
ix=1
iy=1

# nilai posisi
x=1
y=1

while(iy<=t):
    ix=1 # setiap baris dikerjakan dari x paling kiri
    x=y # x paling kiri dari setiap baris adalah hasil penjumlahan atas dan b
    while(ix<=l):
        print(x, end=" ")
        x+=a
        ix+=1
    print()
    iy+=1
    y+=b # pada proses perulangan pertama, ini adalah indeks (1,2) di bawah angka 1 pertama

# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 16 September 2022
# Deskripsi : Modul 2 (For Loop dan While Loop), Modul 3 (Array)

# Loop For
a=int(input("Masukkan nilai a: "))
b=int(input("Masukkan nilai b: "))

for i in range (a,b+1):
    print("Masuk")
    print(i)

# range (a,b,c)  # a a+c ... a+(n.c)<=b-1
# range (a,b)    # a a+1 ... a+(n.1)=b-1
# range (b)      # 0 0+1 ... 0+(n.1)=b-1
range (10)       # 0 1 2 3 4 5 6 7 8 9
range (2,5)      # 2 3 4
range (7,2,-1)   # 7 6 5 4 3
range (2,8,2)    # 2 4 6 8


# Pengulangan Bersarang
n=int(input("Jumlah pengulangan bersarang: "))

for i in range (n):
    for j in range (n):
        print("*", end="")
    print()

# Array
n=int(input("Masukkan nilai range array: "))
x=[0 for i in range (n)]
print(x)
x=["*" for i in range (100)]
print(x)

# Mengganti nilai array
tabel=[0 for i in range (10)]
tabel[2]=int(input("Ganti nilai tabel untuk indeks kedua: "))
print(tabel)

# Mengganti nilai array (banyak)
for i in range (5):
    tabel[i]=int(input("Masukkan nilai ke-"+str(i)+": "))
print(tabel)

# Matriks (Array 2 Dimensi)
a=[[0 for i in range (3)] for i in range (2)]
print(a)

for j in range (2):
    for i in range (3):
        a[j][i]=int(input("Masukan nilai ke ("+str(j)+","+str(i)+"):"))
print(a)

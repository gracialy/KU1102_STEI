# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : November 2022
# Deskripsi : Program mengonversi bilangan sebanyak n kali dengan aturan konversi ke-(bilangan ganjil) menggunakan fungsi pertama dan seterusnya; input: x nilai yang akan dikonversi, n kali konversi; output: hasil akhir

# KAMUS
# x, n: int
# i, value: int

def f1(x):
    # jika x positif, keluaran fungsi adalah -x
    if (x>0):
        return (-x)
    # jika x negatif atau nol, keluaran fungsi adalah x
    else:
        return (x)

def f2(x):
    # jika x genap, keluaran fungsi adalah -2x+1
    if (x%2==0):
        return -(2*x)+1
    # jika x ganjil, keluaran fungsi adalah x-1
    else: 
        return x-1

# ALGORITMA PROGRAM UTAMA
x=int(input("Masukkan nilai x: "))
n=int(input("Masukkan nilai n: "))

i=1
value=x
while i<=n:
    if (i%2==1):
        value=f1(value)
        # debugging station
        # print(i, value)
    else:
        value=f2(value)
        # debugging station
        # print(i, value)
    i+=1

print("Hasil akhir adalah", str(value)+".")
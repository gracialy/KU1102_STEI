# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   :
# Deskripsi : Program mencetak hasil fungsi f(x); input: koefisien a, pangkat b, nilai x; output: hasil f(x)

# KAMUS
# a, b, x: int
# sum: float

# ALGORITMA
a=int(input("Masukkan a: ")) # asumsikan a>0
b=int(input("Masukkan b: "))
x=int(input("Masukkan c: "))

# untuk f(x)=a*(x**b) + (a-1)*(x**(b-1)) + (a=2)*(x**(b-2)) + ... + x**(b-...)
sum=0.0

while (a>0):
    sum = sum + a*(x**b)
    a -= 1
    b -= 1

print(f"f(x) = {sum}")
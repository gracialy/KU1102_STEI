# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 7 November 2022
# Deskripsi : Program 

# KAMUS
# a, b, n: int
# i, h, luas, sigma: float

# ALGORITMA
def f(x):
    return (x**4)+3*(x**3)+5*(x**2)+x+8

a=int(input("Masukkan nilai a: "))
b=int(input("Masukkan nilai b: "))
n=int(input("Masukkan nilai n: "))

h=(b-a)/n

'''luas=0.0
while a<b: #bug exit loop di a!=b
    # maka asumsi b adalah kelipatan dari a+n*delta
    luas+=h /2 * (f(a)+f(a+h))
    a += h
'''
# OR
sigma=0.0
i=a+h
while i<b:
    sigma+=f(i)
    i+=h
luas = h/2 * (f(a)+ 2*sigma +f(b))

print("Hasilnya adalah", luas)
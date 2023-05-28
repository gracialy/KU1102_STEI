
def kuadrat (x):
    x=x*x
    return x

# FUNGSI DEF
def kuadrat (x):
    x2=x*x
    return x2
print(kuadrat(3))

# is actually    
n=int(input("angka untuk dikuadratkan: "))
n2=kuadrat(n)
print(n2)

def pangkat (a,b):
    # asumsi b>=0
    c=1
    for i in range (b):
        c*=a # (c=c*a)
    return c
print(pangkat(3,2))

# driver (to call)
a=int(input("Masukkan nilai a: "))
b=int(input("Masukkan nilai b: "))
print(pangkat(a,b))

def pangkatFloat (a,b):
    c=a**b
    return c
print(pangkatFloat(4,1/2))

# PROSEDUR
print("Menu:")
print("1. Burger")
print("2. Ayam geprek")
print("3. Mie instan: ")
print("Masukkan pilihan: ")
pilihanMakanan=int(input())

print("Menu:")
print("1. Jus alpukat")
print("2. Thai tea")
print("3. Teh tarik")
print("Masukkan pilihan: ")
pilihanMinuman=int(input())

print("Menu:")
print("1. Kentang")
print("2. Kerupuk")
print("3. Abon")
print("Masukkan pilihan: ")
pilihanTambahan=int(input())

# is atually
def tulisMenu (pil1, pil2, pil3):
    print("Menu:")
    print("1. " + str(pil1))
    print("2. " + str(pil2))
    print("3. " + str(pil3))
    print("Masukkan pilihan: ")

tulisMenu("Burger", "Ayam geprek", "Mie instan")
pilihanMakanan=int(input())

tulisMenu("Jus alpukat", "Thai tea", "Teh tarik")
pilihanMinuman=int(input())

tulisMenu("Kentang", "Kerupuk", "Abon")
pilihanTambahan=int(input())

# SUBPROGRAM
# Baku
# Program Test
# Mengetes dungsi kuadratt

# KAMUS
# a: int
# b: int

# Fungsi Kuadrat
def kuadrat (x):
    # menghitung kuadrat x
    hasil=x*x
    return hasil

# ALGORITMA PROGRAM UTAMA
a=5
b=kuadrat(a)+10

# Program Luas Lingkaran
# Menghitung luas lingkaran berdasarkan jari-jari

# KAMUS
# r, L: float
# Definisi dan Realisasi Fungsi Linear
def Luas(r):
    # menghasilkan luas lingkaran berdasarkan jari-jari r
    Luas=3.14*r*r
    return (Luas)

# PROGRAM UTAMA
r=float(input())
L=Luas(r) # pemanggilan fungsi luas
print(L)

# Fungsi Max 2
def max2(a,b):
    # menghasilkan nilai terbesar
    # antara a dan b

    # KAMUS LOKAL

    # ALGORITMA
    if(a>=b):
        return a
    else: # a<b
        return b
    
print("fungsi maksimum 2")
a=int(input("a: "))
b=int(input("b: "))
print(max2(a,b))

print("fungsi maksimum 3")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
print(max2(a,max(b,c)))
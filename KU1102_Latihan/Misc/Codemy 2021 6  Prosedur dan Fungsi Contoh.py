# Prosedur
# Program cetakSegitiga

# baris 1: 1 kolom
# baris 2: 2 kolom
# ...

def cetakSegitiga(panjang):
    for i in range (panjang):
        for j in range (i+1):
            print("*", end=" ")
        print()
    
cetakSegitiga(3)
print()
cetakSegitiga(5)

# Fungsi
# Program pangkat

def pangkat (x,y):
    hasil=1
    for i in range (y):
        hasil*=x
    return hasil

a=int(input("Masukkan a: "))
b=int(input("Masukkan b: "))
print(pangkat(a,b))
print("Nilai dari a pangkat b adalah", pangkat(a,b))
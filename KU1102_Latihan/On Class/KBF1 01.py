# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   :
# Deskripsi : Program memeriksa menghitung energi kinetik; input: massa benda, kecepatan benda; output: energi kinetik

# KAMUS
# m, v, EK: float

# ALGORITMA
# asumsi input bilangan real positif
m=float(input("Masukkan massa (dalam kg): "))
v=float(input("Masukkan kecepatan (dalam m/s2): "))

EK=1/2*m*v*v

print("Energi Kinetik adalah", EK)
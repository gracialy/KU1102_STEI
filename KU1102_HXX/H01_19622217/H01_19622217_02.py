# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 15 September 2022
# Deskripsi : Program memeriksa penempatan kelas; input: tiga digit terakhir NIM; output: kelas

# KAMUS
# akhiranNIM : integer
# kelas      : string

# ALGORITMA
# Input (tiga angka terakhir NIM)
# catatan: 001 dapat ditulis sebagai 1
akhiranNIM=int(input("Masukkan akhiran NIM: "))

# Percabangan
if(1<=akhiranNIM<=100):
    if(akhiranNIM%2==1):        # NIM Ganjil
        kelas="K1"
    else: # (akhiranNIM%2==0)   # NIM Genap
        kelas="K2"
elif(101<=akhiranNIM<=200):
    if(akhiranNIM%2==1):
        kelas="K3"
    else: # (akhiranNIM%2==0)
        kelas="K4"
elif(201<=akhiranNIM<=300):
    if(akhiranNIM%2==1):
        kelas="K5"
    else: # (akhiranNIM%2==0)
        kelas="K6"
elif(akhiranNIM>300):
    if(akhiranNIM%2==1):
        kelas="K7"
    else: # (akhiranNIM%2==0)
        kelas="K8"

# Output
print("Mahasiswa masuk ke kelas", kelas)
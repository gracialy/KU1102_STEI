# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 15 September 2022
# Deskripsi : Program menghitung selang waktu; input: waktu mulai, waktu selesai; output: durasi waktu

# KAMUS
# jamMulai, menitMulai, detikMulai       : integer
# jamSelesai, menitSelesai, detikSelesai : integer
# selangJam, selangMenit, selangDetik    : integer

# ALGORITMA
# Input
print("Masukkan waktu mulai!")
jamMulai=int(input("Jam    : "))
menitMulai=int(input("Menit  : "))
detikMulai=int(input("Detik  : "))
print("Masukkan waktu selesai!")
jamSelesai=int(input("Jam    : "))
menitSelesai=int(input("Menit  : "))
detikSelesai=int(input("Detik  : "))

# Percabangan
# catatan: asumsi tidak ada pergantian hari
# catatan: waktu mulai selalu lebih dulu dari waktu selesai

# selang waktu = waktu selesai - waktu mulai
selangJam=jamSelesai-jamMulai
selangMenit=menitSelesai-menitMulai
selangDetik=detikSelesai-detikMulai

# perbaikan kasus waktu selesai 'lebih kecil' dari waktu mulai dengan 'meminjam' satuan yang lebih besar
# contoh kasus: 01.02.03 sampai 02.01.00
if(selangDetik<0): # detik selesai 'lebih kecil' dari detik mulai, maka meminjam 1 menit=60 detik
    selangMenit=selangMenit-1
    selangDetik=selangDetik+60
if(selangMenit<0): # menit selesai 'lebih kecil' dari detik mulai, maka meminjam 1 jam=60 menit
    selangJam=selangJam-1
    selangMenit=selangMenit+60

# Output
if(selangJam==0):
    print("Tuan Riz berlari selama", str(selangMenit), "menit", str(selangDetik), "detik")
else: # (selangMenit==0 or selangDetik==0 or selangJam!=0)
    print("Tuan Riz berlari selama", str(selangJam), "jam", str(selangMenit), "menit", str(selangDetik), "detik")
# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 04 Oktober 2022
# Deskripsi : Program memeriksa nilai input lebih besar dari input sebelumnya lalu menterminasi program jika nilai tersebut sudah tidak lebih besar berturut-turut sebanyak 3 kali; input: bilangan bulat; output: jumlah dari bilangan yang lebih besar dari input sebelumnya

# KAMUS
# count, repo, sum: int
# bil: int
# over: bool
# i: int

# ALGORITMA
count = 0 # (var) banyak kemunculan angka yang lebih kecil dari angka tepat sebelumnya
over = False # (var) kondisi penghentian program

repo = 0 # (var) menyimpan angka sebelumnya
sum = 0 # (var) menghitung angka yang memenuhi syarat (lebih besar dari angka tepat sebelumnya)

i = 1 # (var) indeks angka ke-i

while (over==False):
    bil = int(input("Angka ke-"+str(i)+": "))
    
    # (percabangan) membandingkan angka dengan angka tepat sebelumnya
    if (i==1 or bil<=repo): # angka pertama otomatis tidak membesar (belum ada pembanding)
        count += 1
    elif (bil>repo):
        count = 0
        sum += bil

    # (percabangan) mengaktifkan var over setelah pelanggaran 3 kali berturut-turut
    if (count==3):
        over=True
    # else: (count!=3)
        # tidak ada yang berubah (program terus berjalan)
    
    repo = bil
    i += 1

print(f"Jumlah nilai yang membesar adalah {sum}.")
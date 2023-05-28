# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 04 Oktober 2022
# Deskripsi : Program memeriksa bilangan faktor-faktor dari bilangan untuk menentukan bilangan sempurna; input: bilangan; output: bilangan sempurna atau bukan

# KAMUS
# bil, sum: int
# i: int

# ALGORITMA
bil = int(input("Masukkan bilangan: ")) # asumsi bil>0

sum = 0 # (var) menyimpan jumlah dari faktor-faktor bilangan (kec. dirinya sendiri)

# (loop) memeriksa faktor dari bilangan sampai sebelum bilangan itu sendiri
for i in range (1,bil):
    # (percabangan) saat i merupakan faktor dari bilangan (habis dibagi)
    if (bil%i==0):
        sum += i
    # else: (bil%i!=0) saat i bukan merupakan faktor dari bilangan
        # i tersebut tidak ikut dihitung

# (percabangan) membandingkan jumlah faktor-faktor dengan bilangan
if (sum==bil):
    print("Bilangan tersebut adalah bilangan sempurna.")
else: # (sum!=bil)
    print("Bilangan tersebut bukan bilangan sempurna.")
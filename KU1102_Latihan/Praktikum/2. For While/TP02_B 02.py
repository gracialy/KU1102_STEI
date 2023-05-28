# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 05 Oktober 2022
# Deskripsi : Program bilangan prima pada selang

# KAMUS
# a, b, count, check: int
# i: int
# cont: bool

# ALGORITMA
a = int(input("Masukkan a: "))
b = int(input("Masukan b: "))

count = 0 # (var) jumlah bilangan prima dalam selang [a,b]

# (loop) memeriksa angka dalam selang [a,b]
for i in range (a,b+1):
    cont = True # (var) kondisi pemberhentian loop pemeriksa faktor
    check = 2 # (var) faktor pemeriksa sifat prima

    # (percabangan) special case, i=1 harus dipisah karena pemeriksaan dimulai dari 2
    if (i==1 or i==0):
        cont = False
    # else: (i!=1)
        # i!=1 bisa diperiksa dengan loop

    # (loop) memeriksa faktor dari angka dalam selang [a,b]
    while(cont==True):
        # (percabangan) menemukan faktor terkecil dari angka (selain 1)
        if (i%check==0):
            cont = False # (var) kondisi penghentian program
            print(i, check)
        # else: (i%check!=0)
            # check bukan faktor dari i, tidak dilakukan apa-apa

        # (percabangan) jika faktor terkecil dari angka (selain 1) adalah angka itu sendiri, maka angka itu adalah prima
        if (check==i):
            count += 1

        # else: (check!=i)
            # i bukan prima, tidak dilakukan apa-apa

        check += 1

# (percabangan) output jika terdapat bilangan prima dalam selang [a,b] atau tidak
if (count>0):
    print(f"Banyaknya bilangan prima pada selang [{a},{b}] adalah {count}.", end=" ")
    print(f"Bilangan prima terbesar di selang tersebut adalah {i}.")
else: # (count==0)
    print(f"Tidak ditemukan bilangan prima pada selang [{a},{b}].")
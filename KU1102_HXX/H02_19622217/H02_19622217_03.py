# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 04 Oktober 2022
# Deskripsi : Program mengeluarkan faktor-faktor prima dari sebuah bilangan; input: bilangan; output: faktor-faktor primanya

# KAMUS
# bil, check : int
# ans: str
# first, cont: bool
# i: int

# ALGORITMA
bil = int(input("Masukkan n: ")) # asumsi n>1

ans = "Faktor primanya adalah "

first = True # (var) kondisi saat i adalah faktor prima pertama

# (loop) memeriksa apakah i (mulai dari 2 sebagai faktor prima pertama) adalah faktor dari bilangan
for i in range (2,bil+1):
    # (percabangan) saat i merupakan faktor dari bilangan (habis dibagi)
    if (bil%i==0):
        check = 2 # (var) pemeriksa faktor prima
        cont = True # (var) kondisi penghentian program

        # (loop) memeriksa sifat prima dari angka i
        while (cont==True):
            # (percabangan) loop dihentikan jika sudah menemukan faktor dari angka i
            if (i%check==0):
                cont = False
            # else: (i%check!=0):
                # tidak terjadi perubahan apa-apa

            # (percabangan) memeriksa sifat prima i, apakah faktor dari angka i adalah dirinya sendiri? (selain 1)
            if (cont==False and check==i and first==True): # i yang berlaku sebagai prima pertama akan dimasukkan ke var output tanpa tanda koma (,) di depannya
                ans = ans + str(i)
                first=False
            elif(cont==False and check==i and first==False):
                ans = ans + ", " + str(i)

            check += 1

print(ans + ".")
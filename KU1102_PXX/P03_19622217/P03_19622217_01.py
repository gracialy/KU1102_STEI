# NIM/Nama: 19622217/Lydia Gracia
# Tanggal: 26 Oktober 2022
# Deskripsi: Program mencari index kemunculan data x ke N; input: banyak data, nilai data, nilai yang dicari (x), N (kemunculan ke-); output: index bilangan x ke N

# KAMUS
# num, search, order: int
# occ, idx: int
# i, j: int
# arr: array [0..num-1] of int

# ALGORITMA
num=int(input("Masukkan nilai banyak data: "))
# inisiasi array data
arr=[0 for i in range (num)]
# memasukkan nilai data ke array
for i in range (num):
    arr[i]=int(input(f"Masukkan data ke-{i+1}: "))

search=int(input("Masukkan nilai yang dicari: "))
order=int(input("Masukkan nilai N: ")) # kemunculan data yang dicari ke-N

occ=0 # banyak kemunculan data sejauh ini

# pengecekan kemunculan data sepanjang banyak data
# asumsi syarat banyak kemunculan data akan selalu diraih
# while
# selama j sebagai pengecekan index masih memenuhi dan
# jumlah kemunculan masih lebih kecil dari syarat
j=0
while (j<num) and (occ<order):
    # jika data cocok dengan yang dicari
    if (arr[j]==search):
        occ+=1 # kemunculan bertambah 1
    # else:
        # (arr[j]!=search), data tersebut tidak cocok dengan data yang dicari
        # tidak dilakukan apa-apa
    
    # saat jumlah kemunculan cocok dengan yang dicari
    if (occ==order):
        idx=j # index saat banyak kemunculan data dipenuhi
    # else:
        # (occ!=order), banyak kemunculan data belum cocok, terus mencari

    j+=1

print(f"Nilai {search} ke-{order} berada pada indeks {idx}.")
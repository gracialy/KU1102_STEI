# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 19 Oktober 2022
# Deskripsi : Program memilih barang dengan diskon terbesar; input: harga, diskon; output: barang terpilih, besar diskon

# KAMUS
# n, besarDiskon, diskonTerbesar, nomorBarang: int
# i: int
# hargaAwal: array [0..n-1] of int
# diskon: array [0..n-1] of int

# ALGORITMA
n=int(input("Masukkan banyak barang: "))

# menginisiasi array hargaAwal berukuran n
hargaAwal=[0 for i in range (n)]
# memasukkan angka sesuai urutan kiri ke kanan
for i in range (n):
    hargaAwal[i]=int(input("Masukkan harga awal barang ke-"+str(i+1)+": "))

# menginisiasi array diskon berukuran n
diskon=[0 for i in range (n)]
# memasukkan angka sesuai urutan kiri ke kanan
for i in range (n):
    diskon[i]=int(input("Masukkan besar diskon (dalam persen) barang ke-"+str(i+1)+": "))

# variabel penyimpan data diskonTerbesar dan nomorBarang
diskonTerbesar=0
nomorBarang=0
# dibutuhkan karena loop akan terus memeriksa angka dari kiri ke kanan
for i in range (n):
    # variabel besar diskon untuk setiap barang dari kiri ke kanan
    besarDiskon=int(hargaAwal[i]*diskon[i]/100)
    # membandingkan data mana yang lebih besar dan update data jika ada yang lebih besar
    if (besarDiskon>diskonTerbesar):
        diskonTerbesar=besarDiskon
        nomorBarang=i+1
    # else: barang dengan besarDiskon yang sama atau lebih kecil tidak akan di-update

print("Barang", nomorBarang, "memiliki diskon paling besar yaitu", diskonTerbesar)
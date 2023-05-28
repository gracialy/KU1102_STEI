# NIM/Nama: 19622217/Lydia Gracia
# Tanggal: 12 Oktober 2022
# Deskripsi: Program menghitung jumlah pantulan bola sampai ketinggian sebelum 1 meter ; input: tinggi awal, tipe bola; output: banyak pantulan

# KAMUS
# t0, type: int
# ans: str
# n: int
# t: float

# ALGORITMA
t0=int(input("Masukkan ketinggian awal bola: "))
type=int(input("Masukkan tipe bola: "))

ans="Bola akan memantul sebanyak "
n=0 # var menyatakan banyaknya bola memantul
t=t0 #var menyatakan tinggi bola setelah pantulan

# apakah t=1 masih memenuhi? (keyword: sebelum ketinggian)
# loop mencari banyak pantulan sebelum ketinggian 1
while(t>1):
    t=t/type
    n+=1

# n yang diperoleh perlu dikurangi 1 karena n yang diperoleh saat ini menyatakan jumlah pantulan selanjutnya
if(t<=1):
    n-=1
# else: (t>1)
    # t masih pada loop dan belum mencapai percabangan

ans=ans+str(n)+" kali."

print(n)
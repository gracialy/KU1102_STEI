# NIM/Nama: 19622217/Lydia Gracia
# Tanggal: 12 Oktober 2022
# Deskripsi: Program menghitung poin Klub Pengkom pada pertandingan A; input: banyak pertandingan, status permainan (menang, kalah, seri); output: poin

# KAMUS
# n, point: int
# niceTry: bool
# i: int
# stat: str

# ALGORITMA


n=int(input("Masukkan banyak pertandingan: "))

point=0
niceTry=False #var menyatakan pertandingan B sudah gugur (pernah kalah)

for i in range (n):
    stat=input("Masukkan hasil pertandingan ke-"+str(i+1)+": ")

    if((i+1)%2!=0 or niceTry==True): # Kompetisi A, kelipatan ganjil
        if(stat=="W"):
            point+=3
        elif(stat=="D"):
            point+=1
        elif(stat=="L"):
            point+=0
    else: # (i+1)%2==0 Kompetisi B, kelipatan genap
        # pertandingan B sistem eliminasi
        # selama belum tereliminasi, poin pada pertandingan genap tidak digitung (keyword: hitung poin pertandingan A)
        # setelah tereliminasi, pertandingan selanjutnya hanya pertandingan A (poin dihitung)
        if(stat=="L"):
            niceTry=True
                   
print("Poin Klub Pengkom saat ini adalah ", str(point)+".")
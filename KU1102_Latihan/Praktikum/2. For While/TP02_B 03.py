# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 05 Oktober 2022
# Deskripsi : Program memeriksa ...; input: ...; output: ...

# KAMUS
''' NOT CLEARED '''

# ALGORITMA
x = int(input("Masukkan X: ")) # asumsi x%2!=0 and x%5!=0

ditemukan=False
digit=1

while(ditemukan==False):
    angka=1
    while (angka<=9 and ditemukan==False):
        if(digit*angka)%x==0:
            ditemukan=True
        else:
            angka=angka+1
    
    if(ditemukan==False):
        digit=digit*10 +1 # 1 -> 11 -> 111

print("Bilangan cantik terkecil yang habis dibagi", x, "adalah", digit*angka)
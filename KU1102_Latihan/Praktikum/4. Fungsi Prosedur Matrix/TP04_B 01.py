# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 7 November 2022
# Deskripsi : Program isTranspose

# KAMUS
# m1: array of str
# bar1, kol1: int (brs & kol m1)
# i, j: int (indeks)
# transpose: bool
# m2: array of str
# bar2, kol2: int(brs & kol m2)

# ALGORITMA
bar1=int(input("Panjang baris M1: "))
kol1= int(input("Panjang kolom M1: "))
print("Masukkan Matriks M1: ")
m1=[input().split(" ", kol1-1) for i in range (bar1)]

# input several data in a line
# eg1=[int(i) for i in input("Masukkan input: ").split(" ", kol1-1)]
# - still array not matrix
# - split in (kol-1) because it's counting using index and 
#   it returns (kol-1) as x amount (max number of split) 
# {i think so?}
# eg2=[input().split(" ",kol1-1) for i in range (bar1)]
# - int conversion must be done upon an element call

# debugging station
# print(m1)

bar2=int(input("Panjang baris M2: "))
kol2= int(input("Panjang kolom M2: "))
print("Masukkan Matriks M2: ")
m2=[input().split(" ", kol2-1) for i in range (bar2)]

transpose=True # temp assumption, m1 is m2 transposed
if kol1==bar2 and kol2==bar1:
    for i in range (bar1):
        for j in range (kol1):
            if int(m1[i][j])!=int(m2[j][i]): # condition breaks the temp assumption
                transpose=False
else:
    transpose=False

if transpose:
    print("Matriks M2 adalah transpose dari Matriks M1.")
else:
    print("Matriks M2 bukan transposse dari Matriks M1.")

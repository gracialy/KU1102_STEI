P=int(input("Masukkan banyak kelompok P:"))
E=int(input("Masukkan banyak kelompok E:"))
N=int(input("Masukkan banyak kelompok N:"))
G=int(input("Masukkan banyak kelompok G:"))

banyakmobil=P
kelompokG=G
if (E<=G):
    banyakmobil=banyakmobil+E
    kelompokG=G-E
    print("P+E",banyakmobil)
elif (E>G):
    banyakmobil=banyakmobil+G
    banyakmobil=banyakmobil+E-G
    print("P+E",banyakmobil)
    G=0
if (N%2==0):
    banyakmobil=banyakmobil+int(N/2)
    print("P+E+N",banyakmobil)
elif (N%2==1):
    banyakmobil=banyakmobil+(N+1)/2
    kelompokG=kelompokG-1
    print("P+E+N",banyakmobil)
print("G",kelompokG)

if(kelompokG!=0):
    if(kelompokG%2==0):
        banyakmobil=banyakmobil+kelompokG/2
    elif(kelompokG%2==1):
        banyakmobil=banyakmobil+int(kelompokG/2)
    print("P+E+N+G",banyakmobil)
print("Banyak mobil yang dibutuhkan adalah",banyakmobil)
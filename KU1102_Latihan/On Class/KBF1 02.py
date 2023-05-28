# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   :
# Deskripsi : Program mencetak predikat kelulusan; input: ipk, pelanggaran; output: predikat kelulusan

# KAMUS
# ipk: float
# foul: str
# isFoul: bool

# ALGORITMA
# asumsi input 0.00<=ipk<=4.0
ipk=float(input("Masukkan IPK: "))
foul=input("Adakah pelanggaran akademik? (ada/tidak): ")

if (foul=="ada"):
    isFoul=True
elif(foul=="tidak"):
   isFoul=False

if (ipk>=3.5 and isFoul==False):
    print("cum laude")
elif (ipk>=3.0 and isFoul==False):
    print("sangat memuaskan")
elif(isFoul==False):
    print("memuaskan")
else:
    print("Tidak ada predikat")
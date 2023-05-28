# NIM/Nama  : 19622217/Lydia Gracia 
# Tanggal   : 28 September 2022
# Deskripsi : Program memeriksa ; input: ; output:

# KAMUS
# j,m,d: int
# mode: str
# change: int
# ans: str

# ALGORITMA
# Input
print("Keadaan awal:")
j=int(input("Jam: "))
m=int(input("Menit: "))
d=int(input("Detik: "))
mode=input("Mode: ")
change=int(input("Nilai perubahan: "))

# Percabangan
ans = "Waktu sekarang adalah: " # variabel yang menyimpan format output

if (mode=="J"):
    j += change
elif (mode=="M"):
    m += change
elif (mode=="D"):
    d += change

# asumsi minus tidak kurang dari 60
# maaf kak belum sempat untuk minus lebih dari 60 :(
if(d<0):
    m -= 1
    d += 60
    print(j,m,d)
if(m<0):
    j -= 1
    m += 60
    print(j,m,d)
if(j<0):
    j += 24
    print(j,m,d)

if(j>23):
    j -= 24
if(m>59):
    j += 1
    m -= 60
if(d>59):
    m += 1
    d -= 60

# Output
ans = ans + str("{:02d}".format(j)) + ":" + str("{:02d}".format(m)) + ":" + str("{:02d}".format(d))
print(ans)
# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 05 Oktober 2022
# Deskripsi : Program SiapBangJago (Pemeriksaan kelipatan a, b, dan c) untuk n bilangan pertama

# KAMUS
# n, a, b, c: int
# isSiap, isBang, isJago: bool
# ans: str

# ALGORITMA
n = int(input("Masukkan nilai N: "))

a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
c = int(input("Masukkan nilai C: "))

ans = "" # (var) menyimpan format output

# (loop) memeriksa dari 1 sampai n
for i in range (1,n+1):
    isSiap = False # var: menyatakan i kelipatan dari A
    isBang = False # var: menyatakan i kelipatan dari B
    isJago = False # var: menyatakan i kelipatan dari C

    if (i%a==0):
        ans = ans + "Siap"
        isSiap = True
    
    if (i%b==0):
        ans = ans + "Bang"
        isBang = True

    if (i%c==0):
        ans = ans + "Jago"
        isJago = True
    
    if (isSiap== False and isBang==False and isJago==False):
        ans = ans + str(i)

    ans = ans + " "

print(ans)
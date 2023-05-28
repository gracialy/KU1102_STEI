# NIM/Nama  : 19622217/Lydia Gracia 
# Tanggal   : 28 September 2022
# Deskripsi : Program memeriksa kecocokan tas Tuan Kil dengan syarat maskapai; input: tas 1, tas 2, tas 3; output: kelayakan tas Tuan Kil, jenis pelanggaran tas Tuan Kil

# KAMUS
# a, b, c: int
# whole, cabin: int
# ans: str
# good: bool
# bad1, bad2: bool
# prev: bool

# ALGORITMA
# Input
a=int(input("Masukkan berat tas A: "))
b=int(input("Masukkan berat tas B: "))
c=int(input("Masukkan berat tas C: "))

whole=int(input("Masukkan batasan berat tas keseluruhan: "))
cabin=int(input("Masukkan batasan berat tas yang dibawa ke kabin: "))

# Percabangan
ans="Tuan Kil " # variabel yang menyimpan format output
good=True # variabel yang menyimpan kelayakan tas Tuan Kil
bad1=False # variabel yang menunjukkan Tuan Kil telah melanggar aturan 1
bad2=False # variabel yang menunjukkan Tuan Kil telah melanggar aturan 2
prev = False # variabel yang menunjukkan Tuan Kil sudah melanggar sebelumnya 

if(a+b+c>whole):
    good = False
    bad1 = True 

if(a>cabin and b>=cabin and c>=cabin):
    good = False
    bad2 = True 

if(good==True): # setelah dicek, tas Tuan Kil memenuhi kedua syarat
    ans = ans + "memenuhi "
else: # (good==False) # setelah dicek, tas Tuan Kil ada yang melanggar syarat
    ans = ans + "melanggar peraturan "
    if(bad1==True):
        ans = ans + "1 "
        prev = True
    if(bad2==True):
        if(prev==True):
            ans = ans + "dan "
        ans = ans +"2 "
ans = ans + "kebijakan maskapai."

# Output
print(ans)
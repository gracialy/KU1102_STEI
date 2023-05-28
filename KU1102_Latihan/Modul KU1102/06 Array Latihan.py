'''# 1
# Program kaliAnggota

# KAMUS
# t: array [0..19] of int
# i, x: int

# ALGORITMA
# deklarasi array t
t=[0 for i in range (20)]

# update nilai anggota t dari input
for i in range (20):
    t[i]=int(input(f"Masukkan t anggota ke-{i+1}: "))

print(t)

x=int(input("Faktor pengali"))

# update nilai anggota t dikali x
for i in range (20):
    t[i]=t[i]*3

print(t)'''

'''# 2
# Program lulusTak

# KAMUS
# nilai: array [0..49] of str
# i, tak, lulus: int


# ALGORITMA
# asumsi nilai A, B, C, D, atau E

# deklarasi array nilai
nilai=["" for i in range (50)]

lulus=0
tak=0

# update elemen array nilai
for i in range (50):
    nilai[i]=input(f"Masukkan nilai ke-{i+1}: ")

    if (nilai[i]=="D" or nilai[i]=="E"):
        tak+=1
    else:
        lulus+=1

print("lulus", lulus)
print("tak lulus", tak)'''

'''# 3
# Program minArray
# Mencari nilai terkecil pada array

# KAMUS
# N : int
# T : array [0..N-1] of int
# i : int
# min : int

# ALGORITMA
N = 10 # assign N dengan ukuran T

T=[0 for i in range (N)]

for i in range (N):
    T[i]=int(input(f"Masukkan nilai ke-{i+1}: "))

# Mencari nilai maksimum
min = T[0] # init min dgn elemen pertama

# Pencarian dimulai dari elemen ke-2
for i in range(1,N):
    # jika ada elemen < min, ganti nilai min
    if (T[i] < min):
        min = T[i]
        # Cetak nilai terbesar
print ("Nilai terkecil = " + str(min))'''

'''# 4
# Program indeksTerakhir
# Mencari indeks di mana X ditemukan terakhir kali di T

# KAMUS
# N : int; ukuran T
# T : array [0..N-1] of int
# i, X : int
# found : bool; menentukan X sdh ditemukan/belum

# ALGORITMA
N = 3 # assign N dengan ukuran T
T=[0 for i in range (N)]

for i in range (N):
    T[i]=int(input(f"Masukkan nilai ke-{i+1}: "))

# Membaca nilai yang dicari, yaitu X
X = int(input())

i = -1
found = False # found = False; X belum ditemukan

while (-i <= N and found == False):
    if (T[i]==X):
        found=True
    else:
        i-=1

# Cetak Hasil
if (found == True): # X ditemukan di T
    print (str(X) + " ditemukan di indeks ke-" + str(N-(-i))) # indeks ke N-(-i) untuk mengonversi indeks min ke indeks normal
else: # found = False; X tidak ditemukan di T
    print (str(X) + " tidak ditemukan")'''

'''# 5
# Program penjumlahanVektor

N = 5 # assign N dengan ukuran T

v=[0 for i in range (N)]

for i in range (N):
    v[i]=int(input(f"Masukkan nilai ke-{i+1}: "))

u=[0 for i in range (N)]

for i in range (N):
    u[i]=int(input(f"Masukkan nilai ke-{i+1}: "))

# w
w=[0 for i in range (N)]

for i in range (N):
    w[i]=v[i]+u[i]

print(w)'''

# 6
# Program BMKG

N = 5 # assign N dengan ukuran T

temp=[0 for i in range (N)]

for i in range (N):
    temp[i]=float(input(f"Masukkan nilai ke-{i+1}: "))

# avg
sum=0
for i in range (N):
    sum+=temp[i]

avg=sum/N
print("Rata rata", avg)

# min
min=temp[0]
for i in range (N):
    if (temp[i]<min):
        min=temp[i]

print("Minimal", min)

# >=30
print("Suhu di atas 30 derajat Celcius pada tanggal: ")
for i in range (N):
    if (temp[i]>=30):
        print(str(i+1)+" September 2018")


# first <15
found=False
i=0
while (found==False and i<N):
    if (temp[i]<=15.0):
        found=True
    else:
        i+=1
    
if (found==True):
    print("Suhu di bawah 15 derajat Celcius pertama kali terjadi pada tanggal", i+1, "September 2018")
else:
    print("Suhu tidak pernah di bawah 15 derajat Celcius")
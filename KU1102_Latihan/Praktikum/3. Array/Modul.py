'''# 3.2.1
# Program reverseBil

# KAMUS
# arrayN : array [0..n-1] of int
# i: int

# ALGORITMA
n=int(input("Masukkan N: "))
arrayN=[0 for i in range (n)] # indeks dari 0 sampai n-1
# artinya data sebanyak n buah

# ubah data dari anggota array tadi
for i in range (n):
    arrayN[i]=int(input())

# mulai panggil dari indeks ke n-1 (karena indeks terakhir adalah n-1)
# batas akhir -1 karena kita akan panggil sampai indeks 0
for i in range (n-1,-1,-1):
    print(arrayN[i], end=" ")'''

'''# 3.2.2
# Program anagramBil
# setiap elemen dapat disusun menjadi susunan baru

# KAMUS
# a, b: int
# arrayA: array [0..a-1] of int
# freqA, freqB: array [0..9] of int
# arrayB: array [0..b-1] of int
# i, value: int

# ALGORITMA
# asumsi elemen a dan b <=10

a=int(input("Masukkan banyaknya elemen A: "))
arrayA=[0 for i in range (a)]
freqA=[0 for i in range (10)] # deklarasi tabel frekuensi

for i in range (a):
    arrayA[i]=int(input(f"Masukkan elemen A ke-{i}: "))

# tabel frekuensi
for i in range (a):
    value=arrayA[i] # mengakses nilai dari input a ke-i
    freqA[value-1]=freqA[value-1]+1 # memperbarui frekuensi dari bilangan value

# debugging station
# print(freqA)

b=int(input("Masukkan banyaknya elemen B: "))
arrayB=[0 for i in range (a)]
freqB=[0 for i in range (10)]

for i in range (b):
    arrayB[i]=int(input(f"Masukkan elemen B ke-{i}: "))

for i in range (b):
    value=arrayB[i]
    freqB[value-1]=freqB[value-1]+1

if (a==b):
    if (freqA==freqB):
        print("B adalah anagram dari A")
    else:
        print("B bukan anagram dari A")
else:
    print("B bukan anagram dari A")'''
'''
# 3.2.3
# Program palindromStr
# terbaca sama dari depan dan belakang

# KAMUS
# length: int
# string: str
# i: int
# arrayStr, reverseStr: array [0..length-1] of str

# ALGORITMA
# asumsi string hanya berisi huruf kecil
length=int(input("Masukkan panjang string: "))
string=input("Masukkan string: ")

# reverse array
arrayStr=[string[i] for i in range (length)] # string dapat diperlakukan seperti array
reverseStr=[string[i] for i in range (length-1,-1,-1)]

if (arrayStr==reverseStr):
    print(string, "adalah palindrom")
else:
    print(string, "bukan palindrom")'''
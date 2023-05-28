# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 19 Oktober 2022
# Deskripsi : Program memeriksa kemunculan substring pada string lain; input: panjang substring, substring, panjang string induk, string induk; output: banyak kemunculan

# KAMUS
# len1, len2, kemunculan: int
# str1, str2: array
# muncul: bool
# i, j: int

# ALGORITMA
# asumsi kedua string terdiri dari huruf kecil saja
len1=int(input("Masukkan panjang string 1: "))
str1=input("Masukkan string 1: ")

len2=int(input("Masukkan panjang string 2: "))
str2=input("masukkan string 2: ")

# variabel yang menyimpan banyak kemunculan str1 di str2
kemunculan=0

# asumsi len1<=len2
# periksa str2 dari indeks 0 sampai indeks len2-len1+1
# indeks setelahnya tidak mungkin mengandung str1, karena sisa str2 < len1
for i in range (len2-len1+1):
    muncul=True # variabel kondisi ada kemunculan str1 di str2 atau tidak
    j=0
    # pemeriksaan diulang selama belum ada bagian yang berbeda dan huruf pada str1 belum diperiksa seluruhnya
    while (j<len1 and muncul):
        # string dapat diperlakukan seperti array
        # memeriksa huruf dengan indeks [i+j] di str2
        # dimulai dari indeks i dari loop for, diulangi sebanyak len1 kali yang direpresentasikan dengan indeks j
        # hingga str1 diperiksa seluruhnya
        if (str2[i+j]!=str1[j]):
            muncul=False
        # else: karakter string1 cocok dengan string2, pemeriksaan dilanjutkan
        j+=1
    # lolos dari pemeriksaan (dapat mempertahankan nilai muncul==True)
    # artinya ada bagian di str2 yang mengandung str1
    if (muncul):
        kemunculan+=1
    # else: tidak ada yang cocok, tidak dilakukan apa-apa

print("String 1 muncul sebanyak", kemunculan, "kali.")

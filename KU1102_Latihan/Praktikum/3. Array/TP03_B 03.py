# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 19 Oktober 2022
# Deskripsi : 

# KAMUS


# ALGORITMA
len1=int(input("Panjang kata pertama: "))
str1=input("Kata pertama: ")

len2=int(input("Panjang kata kedua: "))
str2=input("Kata kedua: ")

sambungan=""
count1=0
count2=0

while (count1<len1 and count2<len2):
    if (str1[count1]==str2[count2]):
        sambungan+=str1[count1]
        count2+=1
    else:
        if (sambungan!=""): # jika sudah pernah ada karakter yang cocok
            count1-=1 # ulang mencocokkan dari karakter tadi di str1
            # ilustrasi: ayamayamy - ayamy
            # mis: perulangan sudah sampai pada karakter "ayam" (kemunculan "ayam" pertama dari str1) memenuhi syarat
            # namun selanjutnya "a"!="y" sehingga tidak memenuhi syarat
            # reset pengecekan str1 pada karakter "a" tadi terhadap str2 dari karakter pertama "a"
            # pengecekan sesuai sampai akhir str1 sehingga sambungannya adalah "ayamy"
        sambungan="" # memperbarui sambungan kata (ternyata tidak cocok)
        count2=0 # patokan ulang terhadap karakter pertama str2
    count1+=1
    # debugging station
    # print(sambungan, count1, count2)

if (sambungan==""):
    print("Kedua kata tidak dapat disambung.")
else: # terdapat isi dalam sambungan
    print(f"Kedua kata dapat disambung dengan substr '{sambungan}'.")
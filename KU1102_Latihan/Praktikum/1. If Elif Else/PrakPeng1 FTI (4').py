# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : 27 September 2022
# Deskripsi : Program mengelompokkan level mudah, sedang, dan sulit serta memeriksa apakah game sudah memenuhi syarat kesulitan; input: jumlah pemain, jumlah pemain yang berhasil; output: jumlah level mudah, sedang, dan sulit, keberhasilan game

# KAMUS
# all1, success1, all2, success2, all3, success3, all4, success4, all5, success5: int
# isEasy, isMed, isHard: int

# ALGORITMA
# Input
all1=int(input("Banyak pemain yang memainkan level 1: "))
success1=int(input("Banyak pemain yang berhasil menyelesaikan level 1: "))
all2=int(input("Banyak pemain yang memainkan level 2: "))
success2=int(input("Banyak pemain yang berhasil menyelesaikan level 2: "))
all3=int(input("Banyak pemain yang memainkan level 3: "))
success3=int(input("Banyak pemain yang berhasil menyelesaikan level 3: "))
all4=int(input("Banyak pemain yang memainkan level 4: "))
success4=int(input("Banyak pemain yang berhasil menyelesaikan level 4: "))
all5=int(input("Banyak pemain yang memainkan level 5: "))
success5=int(input("Banyak pemain yang berhasil menyelesaikan level 5: "))

# variabel untuk menyimpan banyak level per kategori
isEasy=0
isMed=0
isHard=0

# Proses (Percabangan)
if (success1>=80/100*all1):
    isEasy += 1 # ada soal yang memenuhi syarat level mudah, level mudah bertambah satu
elif(success1>=30/100*all1):
    isMed += 1 # seperti logic di atas untuk kasus level sedang
elif(success1<30/100*all1):
    isHard += 1

if (success2>=80/100*all2):
    isEasy += 1
elif(success2>=30/100*all2):
    isMed += 1
elif(success2<30/100*all2):
    isHard += 1

if (success3>=80/100*all3):
    isEasy += 1
elif(success3>=30/100*all3):
    isMed += 1
elif(success3<30/100*all3):
    isHard += 1

if (success4>=80/100*all4):
    isEasy += 1
elif(success4>=30/100*all4):
    isMed += 1
elif(success4<30/100*all4):
    isHard += 1

if (success5>=80/100*all5):
    isEasy += 1
elif(success5>=30/100*all5):
    isMed += 1
elif(success5<30/100*all5):
    isHard += 1

# Output
print(f"Banyak level yang mudah sebanyak {isEasy}, level sedang sebanyak {isMed}, dan level sulit sebanyak {isHard}.")

if (isEasy>=2 and isHard>=1):
    print("Target berhasil dicapai.")
else: # (isEasy<2 or isHard<1)
    print("Target gagal dicapai.")
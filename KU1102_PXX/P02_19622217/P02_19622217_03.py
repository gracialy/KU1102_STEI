# NIM/Nama: 19622217/Lydia Gracia
# Tanggal: 12 Oktober 2022
# Deskripsi: Program menggolongkan ruang makan sesuai dengan nomor kamar; input: nomor kamar, output: ruang makan

# KAMUS
# num, digit, breakdown: int
# ans: str

# ALGORITMA
num=int(input("Masukkan nomor kamar: "))

ans="Kamar "+str(num)+" akan termasuk dalam ruang makan "

print (num, end=" ")

# loop hingga hitungan digit tidak lebih dari 10
while(num>=10):
    breakdown=num #var agar bebas mendekomposisi num
    digit=0 #var jumlah digit dari num saat ini
    # menghitung jumlah digit dari input angka sebelumnya
    while(breakdown>=10):
        digit = digit + int(breakdown%10)
        breakdown = int(breakdown//10)
    digit+=breakdown
    num=digit
    print("->", num, end=" ")
print()

ans=ans+str(num)+"."

print(ans)



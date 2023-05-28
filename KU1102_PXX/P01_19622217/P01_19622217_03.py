# NIM/Nama  : 19622217/Lydia Gracia 
# Tanggal   : 28 September 2022
# Deskripsi : Program memeriksa ; input: ; output:

# KAMUS
# milk, syrup, ice: int
# porsi, ml_m, ml_s, ml_i: int
# sum_bag, bag_m, bag_s, bag_i: int
# banyak: int

# ALGORITMA
# Input
milk=int(input("Masukkan bagian Susu: "))
syrup=int(input("Masukkan bagian Sirup: "))
ice=int(input("Masukkan bagian Es: "))

porsi=int(input("ml per porsi: "))
ml_m=int(input("Masukkan ml banyak Susu: "))
ml_s=int(input("Masukkan ml banyak Sirup: "))
ml_i=int(input("Masukkan ml banyak Es: "))

# Percabangan
sum_bag = milk+syrup+ice # variabel yang mencari jumlah bagian dari setiap perbandingan komponen

# dengan menggunakan konsep: perbandingan dit. / perbandingan dik. * nilai dik, = nilai dit.
# perbandingan dit.: komponen yang ingin dicari dapat dibagi menjadi berapa bagian
# nilai dik: nilai dari jumlah setiap perbandingan komponen (porsi)
# perbandingan dik.: jumlah bagian dari setiap komponen (sum_bag)
bag_m = int(ml_m // ((milk/sum_bag)*porsi)) # variabel menunjukkan susu dapat dibagi menjadi bag_m bagian
bag_s = int(ml_s // ((syrup/sum_bag)*porsi)) # variabel menunjukkan sirup dapat dibagi menjadi bag_s bagian
bag_i = int(ml_i // ((ice/sum_bag)*porsi)) # variabel menunjukkan ess dapat dibagi menjadi bag_i bagian

# mengecek bagian susu, sirup, dan es terkecil yang merupakan jumlah maksimum minuman yang dapat diracik
if (bag_m<=bag_s and bag_m <= bag_i):
    banyak=bag_m
elif(bag_s<=bag_m and bag_s<=bag_i):
    banyak=bag_s
elif(bag_i<=bag_m and bag_i<=bag_s):
    banyak=bag_i

# Output
print("Tuan Kil dapat membuat", banyak, "porsi minuman.")
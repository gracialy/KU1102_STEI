# 02

# KAMUS
# penghasilan: float
# bulan: int
# pajak, denda: float

# INPUT
penghasilan=int(input("Masukkan jumlah penghasilan (dalam juta): "))
bulan=int(input("Masukkan banyaknya bulan: "))

# ALGORITMA
if(0<penghasilan<=50):
    pajak=5/100*penghasilan
elif(penghasilan<=250):
    pajak=15/100*penghasilan
elif(penghasilan<=500):
    pajak=25/100*penghasilan
elif(penghasilan>500):
    pajak=35/100*penghasilan
print(pajak)

denda=pajak*12/100
if (denda>150):
    denda=150
print(denda)
print(denda*(bulan-1))

if(bulan>1):
    pajak=(pajak*bulan)+(denda*(bulan-1))

# OUTPUT
print("Total pajak yang harus dibayarkan adalah", int(pajak*1000000))

# test case 3 in the module is wrong
# 02
# bilangan bravo
'''fairly awesome problem'''

# KAMUS
# bilangan: int
# digit1, digit2, digit3, digit4: int
# jumlahDigit: int
# bravo: bool

# INPUT
bilangan=int(input("Masukkan sebuah bilangan: "))

# ALGORITMA
# menguraikan bilangan menjadi digit-digit
# asumsi bilangan terdiri dari 4 digit
digit1=bilangan//1000
digit2=bilangan//100-digit1*10
digit3=bilangan//10-digit1*100-digit2*10
digit4=bilangan%10

jumlahDigit=digit1+digit2+digit3+digit4

if(digit1==0):
    bravo=True
    
if(digit2==0):
    bravo=True
    
if(digit3==0):
    bravo=True
    
if(digit4==0):
    bravo=True

if(digit1!=0 and jumlahDigit%digit1==0):
    bravo=True
elif(digit1!=0 and jumlahDigit%digit1!=0):
    bravo=False
    
if(digit2!=0 and jumlahDigit%digit2==0):
    bravo=True
elif(digit2!=0 and jumlahDigit%digit2!=0):
    bravo=False
    
if(digit3!=0 and jumlahDigit%digit3==0):
    bravo=True
elif(digit3!=0 and jumlahDigit%digit3!=0):
    bravo=False
    
if(digit4!=0 and jumlahDigit%digit4==0):
    bravo=True
elif(digit4!=0 and jumlahDigit%digit4!=0):
    bravo=False

# OUTPUT
# bilangan bravo: jumlah digit habis dibagi oleh setiap digitnya
if(bravo==True):
   print("Bilangan tersebut adalah bilangan Bravo.")
elif(bravo==False):
   print("Bilangan tersebut adalah bilangan biasa.")
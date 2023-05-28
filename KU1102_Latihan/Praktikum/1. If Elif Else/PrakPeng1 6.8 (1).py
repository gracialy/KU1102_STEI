# 01
# ukuran baju

# INPUT
lebarBahu=int(input("Masukkan ukuran lebar bahu: "))
panjangBaju=int(input("Masukkan panjang baju: "))
ukuranLingkar=int(input("Masukkan ukuran lingkar baju: "))

# ALGORITMA
if (lebarBahu<=10):
    if (panjangBaju<=40):
        if (ukuranLingkar<=90):
            baju="S"
        elif (ukuranLingkar<=120):
            baju="M"
        elif (ukuranLingkar<=180):
            baju="L"
        elif (ukuranLingkar<=220):
            baju="XL"
    elif(panjangBaju<=60):
        if (ukuranLingkar<=120):
            baju="M"
        elif (ukuranLingkar<=180):
            baju="L"
        elif (ukuranLingkar<=220):
            baju="XL"
    elif(panjangBaju<=80):
        if (ukuranLingkar<=180):
            baju="L"
        elif (ukuranLingkar<=220):
            baju="XL"
    elif(panjangBaju<=100):
        if (ukuranLingkar<=220):
            baju="XL"  
elif (lebarBahu<=14):
    if(panjangBaju<=60):
        if (ukuranLingkar<=120):
            baju="M"
        elif (ukuranLingkar<=180):
            baju="L"
        elif (ukuranLingkar<=220):
            baju="XL"
    elif(panjangBaju<=80):
        if (ukuranLingkar<=180):
            baju="L"
        elif (ukuranLingkar<=220):
            baju="XL"
    elif(panjangBaju<=100):
        if (ukuranLingkar<=220):
            baju="XL"
elif (lebarBahu<=18):
    if(panjangBaju<=80):
        if (ukuranLingkar<=180):
            baju="L"
        elif (ukuranLingkar<=220):
            baju="XL"
    elif(panjangBaju<=100):
        if (ukuranLingkar<=220):
            baju="XL"
elif (lebarBahu<=25):
    if(panjangBaju<=100):
        if (ukuranLingkar<=220):
            baju="XL"

# OUTPUT
print("Ukuran baju yang tepat adalah", baju)
'''


'''
# 01 v.2
# ukuran baju

# KAMUS
# lebarBahu, panjangBaju, ukuranLingkar: float
# baju: string

# INPUT
lebarBahu=float(input("Masukkan ukuran lebar bahu: "))
panjangBaju=float(input("Masukkan panjang baju: "))
ukuranLingkar=float(input("Masukkan ukuran lingkar baju: "))

# ALGORITMA
if (18<lebarBahu<=22 or 80<panjangBaju<=100 or 180<ukuranLingkar<=220):
    baju="XL"
elif (14<lebarBahu<=18 or 60<panjangBaju<=80 or 120<ukuranLingkar<=180):
    baju="L"
elif (10<lebarBahu<=14 or 40<panjangBaju<=60 or 90<ukuranLingkar<=120):
    baju="M"
if (lebarBahu<=10 and panjangBaju<=40 and ukuranLingkar<=90):
    baju="S"

# OUTPUT
print("Ukuran baju yang tepat adalah", baju)
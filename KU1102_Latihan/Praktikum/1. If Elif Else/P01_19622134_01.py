LebarBahu=int(input("Masukkan ukuran lebar bahu:"))
PanjangBahu=int(input("Masukkan panjang baju:"))
LingkarBaju=int(input("Masukkan ukuran linggar baju:"))
if (LebarBahu<=10):
    UkuranLEB="S"
elif(LebarBahu<=14 and LebarBahu>10):
    UkuranLEB="M"
elif(LebarBahu<=18 and LebarBahu>14):
    UkuranLEB="L"
elif(LebarBahu<=25 and LebarBahu>18):
    UkuranLEB="XL"

if (PanjangBahu<=40):
    UkuranPB="S"
elif(LebarBahu<=60 and LebarBahu>40):
    UkuranPB="M"
elif(LebarBahu<=80 and LebarBahu>60):
    UkuranPB="L"
elif(LebarBahu<=100 and LebarBahu>80):
    UkuranPB="XL"

if (LingkarBaju<=90):
    UkuranLB="S"
elif(LingkarBaju<=120 and LingkarBaju>90):
    UkuranLB="M"
elif(LingkarBaju<=180 and LingkarBaju>120):
    UkuranLB="L"
elif(LingkarBaju<=220 and LingkarBaju>180):
    UkuranLB="XL"

if(UkuranLEB=="XL" or UkuranPB== "XL" or UkuranLB=="XL"):
    print("Ukuran baju yang tepat adalah XL")
elif(UkuranLEB=="L" or UkuranPB== "L" or UkuranLB=="L"):
    print("ukuran baju yang tepat adalah L")
elif(UkuranLEB=="M" or UkuranPB== "M" or UkuranLB=="M"):
    print("ukuran baju yang tepat adalah M")
elif(UkuranLEB=="S" or UkuranPB== "S" or UkuranLB=="S"):
    print("ukuran baju yang tepat adalah S")

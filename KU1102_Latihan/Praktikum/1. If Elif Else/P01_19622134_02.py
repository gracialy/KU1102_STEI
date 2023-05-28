data=int(input("Masukkan sebuah bilangan:"))
digit1=int(data/1000)
digit2=int((data-digit1*1000)/100)
digit3=int(((data-digit1*1000)-digit2*100)/10)
digit4=int(((data-digit1*1000)-digit2*100)-digit3*10)

total=int(digit1+digit2+digit3+digit4)

if(total%digit1==0 and total%digit2==0 and total%digit3==0 and total%digit4==0):
    print("Bilangan tersebut adalah bilangan Bravo.")
elif(total%digit1!=0 or total%digit2!=0 or total%digit3!=0 or total%digit4!=0):
    print("Bilangan tersebut adalah bilangan biasa.")
'''percabangan salah'''
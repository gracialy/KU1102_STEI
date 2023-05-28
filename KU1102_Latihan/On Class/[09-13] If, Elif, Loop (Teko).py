'''
for i in range (100):
    print (i)
# will print 0-99

a=int(input())
b=int(input())
i=a
while(i<=b):
    print(i)
    i+=1

# while and for difference
# while kita tentukan batasan
# for selama syarat terpenuhi akan terus berjalan

'''
# untuk mendapatkan 4 liter air dari teko 5 liter dan 3 liter
teko_5=0
teko_3=0

print("teko a: ", teko_5)
print("teko b: ", teko_3)

while (teko_5!=4):
    print("Pilihan:")
    print("1. Isi teko 5")
    print("2. Isi teko 3")
    print("3. Tuang teko 5")
    print("4. Tuang teko 3")
    print("5. Buang teko 5")
    print("6. Buang teko 3")
    pilih=int(input("Pilih: "))

    if(pilih==1):
        teko_5=5
    elif(pilih==2):
        teko_3=3
    elif(pilih==3):
        while teko_5!=0 and teko_3!=3:
            teko_3=teko_3+1
            teko_5=teko_5-1
    elif(pilih==4):
        while teko_3!=0 and teko_5!=5:
            teko_5=teko_5+1
            teko_3=teko_3-1
    elif(pilih==5):
        teko_5=0
    elif(pilih==6):
        teko_3=0
    
    print("Teko a: ", teko_5)
    print("Teko b: ", teko_3)
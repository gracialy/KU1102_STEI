# STAT: CLEAR 
'''BRILLIANT'''
# Program PersegiAngka

# ALGORITMA
s=int(input("Masukkan panjang sisi persegi: "))
b=int(input("Masukkan nilai B: ")) # 1+2b 1+b 1 1+b 1+2b

for i in range (s):
    pedoman=i
    for j in range (s):
        if (i==j):
            print(1, end=" ")
        else:
            # selisih posisi ke 1
            if(j>pedoman):
                n=j-pedoman
            else:
                n=pedoman-j
            print(1+b*n, end=" ")
    print()

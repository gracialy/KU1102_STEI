# STAT: CLEAR
'''OMG HEISEI ERA EINSTEIN I FEAR'''
# Program KubusMinimal

# ALGORITMA
n=int(input("Masukkan banyak potongan lego: "))

ans="Tuan Kil dapat membuat "

made=0

while (n>=1):
    i=1
    while (i**3 < n):
        i+=1

    if(i**3>n):
        i-=1

    banyak=n//(i**3)
    made = made + banyak
    n=n-(i**3)*banyak
    print(i**3, banyak, n)

print(made)

# ans= ans + str(made) + " kubus."
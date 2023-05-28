# STAT: CLEAR
# Program CekPerpangkatan

# ALGORITMA
n=int(input("Masukkan bilangan N: "))
k=int(input("Masukkan nilai k: "))

i=0
isPower=False

# apakah n=k**i?
while (k**i <= n):
    if (n==k**i):
        isPower=True
    i+=1

if (isPower==True):
    print(n, "merupakan perpangkatan", str(k) + ".")
else:
    print(n, "bukan merupakan perpangkatan", str(k) + ".")
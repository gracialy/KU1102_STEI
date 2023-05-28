'''
# perulangan bersarang
i=1
while(i<4):
    j=1
    while(j<=i):
        print(j, end=" ")
        j+=1
    print("") # act as \n
    i+=1

# 1
# 1 2
# 1 2 3

# atau
for i in range (1,6):
    for j in range (1,i+1):
        print(j, end=" ")
    print("") # act as \n
'''

'''
# 4.1
# FaktorBil
n=int(input())
print("faktor-faktornya")
i=n

while (i!=0):
    if(n%i==0):
        print(i)
    i-=1
'''

'''
# 4.2
# digitKelipatan9
n=int(input())
sum=0

# menyingkirkan digit terakhir
while(n>10):
    sum = sum + n%10
    n = n//10
sum=sum+n # angka tersisa satuan cukup ditambah
print(sum)

# or
while(n>0):
    sum = sum + n%10
    n = n//10
print(sum)
'''

'''
# 4.3
# akar3Desimal
n=int(input())

root=0
# menebak akar dari 0
for i in range (root**2<n):
    root += 0.001 # ketelitian 3 angka di belakang koma
print(root)
'''

'''
# 4.4
# primaInterval
a=int(input())
b=int(input())

# cek prima
for i in range (a,b+1,1):
    j=2 # memeriksa dari nilai kecil ke besar
    if(i>1): # patokan bilangan prima terkecil
        while(i%j!=0):
            j+=1
    
    if(i==j): # faktor dari bilangan prima hanyalah 1 dan angka itu sendiri
        print(i)
'''

'''
# 4.6
# desainTegel

ukuran=int(input())
diagonal=input()
isi=input()

for i in range (ukuran):
    for j in range (ukuran):
        if(i==j): # diagonal kiri
            print(diagonal, end="")
        elif(i+j==ukuran-1): # diagonal kanan
            print(diagonal, end="")
        else:
            print(isi, end="")
    print("")
'''

'''
# 4.7
# pukupukupowpow
a=int(input())
b=int(input())
c=int(input())

for i in range (2,c+1): # dimulai dari 2 untuk mengilustrasikan perpangkatan b oleh c diselesaikan dari pangkat kedua dan selanjutnya
    b=b*b
a=a**b
print(a)
'''

'''
# 4.8
# deretFibonacci
n=int(input())

a=0
b=1
print(f"0, 1,", end=" ")
for i in range (3,n):
    c=a+b
    print(c, end=", ")
    a=b
    b=c
print(a+b)
'''

'''
# 4.9
# nilaiMax
n=int(input())

max=0

for i in range (n):
    nilai=int(input())
    if(nilai>max):
        max=nilai
    print(max)
'''

'''
# 4.10
# polaDiamond
n=int(input())

for i in range (1,n):
    for j in range (n-i):
        print(" ", end="")
    for j in range (2*i-1):
        print("*", end="")
    for j in range (n-i):
        print(" ", end="")
    print()
for j in range (2*n-1):
    print("*", end="")
print()
for i in range (n-1,0,-1):
    for j in range (n-i):
        print(" ", end="")
    for j in range (2*i-1):
        print("*", end="")
    for j in range (n-i):
        print(" ", end="")
    print()
'''


# 4.11
# primaN
n=int(input())
count=1
cur=2
prime=True

while(count<n):
    cur+=1
    print("checkpoint")
    i=2
    while(i<=cur):
        print("cp2")
        if(cur%i==0):
            print("cp3")
            prime=False
        i+=1
    if(prime):
        count+=1
print(cur)

'''# ERROR'''


'''
# 4.12
# fpb
a=int(input())
b=int(input())

fpb=1
for i in range (2,min(a,b)+1):
    if(a%i==0 and b%i==0):
        fpb=i
print(fpb)
'''
# Program fabc

'''def f(a,b,c):
    return 2*(a**3) + 5*(b**2) - c

a=int(input("Masukkan a: "))
b=int(input("Masukkan b: "))
c=int(input("Masukkan c: "))
print(f"f({a},{b},{c}) = {f(a,b,c)}")'''

# Program fxgx

'''def f(x):
    return 2/3*(x**2) + 5*x + 7

def g(x):
    return x**0.5 + 3/x

x=int(input("Masukkan bilangan x: "))
print(f"f(f(g({x}))) = {f(f(g(x)))}")
print(f"f(g(f({x}))) = {f(g(f(x)))}")
print(f"g(f(f({x}))) = {g(f(f(x)))}")'''

# Program kpkABC

'''def fpb(a,b):
    factor=1
    biggest=1
    while factor<=a and factor<=b:
        if a%factor==0 and b%factor==0:
            biggest=factor
        factor+=1
    return biggest

def kpk(a,b):
    return int(a * b / fpb(a,b))

a=int(input("Masukkan bilangan A: "))
b=int(input("Masukkan bilangan B: "))
c=int(input("Masukkan bilangan C: "))
print(f"KPK dari {a}, {b}, dan {c} adalah {kpk(a,kpk(b,c))}.")

# debugging station
# rint(fpb(b,c))
# print(kpk(b,c))
# print(fpb(a,kpk(b,c)))
# print(kpk(a,kpk(b,c)))'''

# Program pasanganKomposit

'''def compos(x):
    isCompos=False
    if(x>1):
        i=2
        while i<x and not isCompos:
            if (x%i==0):
                isCompos=True
            i+=1
    return isCompos

a=int(input("Masukkan A: "))
b=int(input("Masukkan B: "))
# debugging station
print(compos(a), compos(b))
print("Pasangan bilangan komposit: ")
for i in range (a,b+1):
    for j in range (a,b+1):
        if (compos (i) and compos (j) and compos(i+j) and i<j):
            print(i, j)'''

# Program bilSempurna

'''def perfect(x):
    isPerfect=False
    sum=0
    for i in range (1,x):
        if (x%i==0):
            sum+=i
    if sum==x:
        isPerfect=True
    return isPerfect

a=int(input("Masukkan bilangan A: "))
b=int(input("Masukkan bilangan B: "))
print("Bilangan sempurna: ")
for i in range (a, b+1):
    if perfect(i):
        print(i)'''

# Program heksadesimal

'''hexChar=["0","1","2","3","4","5","6","7","8","9",
        "A","B","C","D","E","F"]

def hexdec(x):
    # hex-puluhan
    idx=0
    while (hexChar[idx]!=x[0]): #find index
        idx+=1
    result=idx*16
    # hex-satuan
    idx=0
    while (hexChar[idx]!=x[1]):
        idx+=1
    result+=idx
    return result

def dechex(x):
    return hexChar[x//16]+hexChar[x%16]

a=input("Masukkan bilangan A: ")
b=input("Masukkan bilangan B: ")
print(f"{a} + {b} = {dechex(hexdec(a)+hexdec(b))}")'''

# Program batasBelanja

'''# Sabun, HandSanitizer, Masker, FaceShield
store=[0 for i in range (4)]
n=int(input("Masukkan jumlah barang yang dibeli: "))

for i in range (n):
    item=input(f"Masukkan barang ke-{i+1}: ")

    if item=="Sabun":
        store[0]+=1
    elif item=="HandSanitizer":
        store[1]+=1
    elif item=="Masker":
        store[2]+=1
    elif item=="FaceShield":
        store[3]+=1

# debugging station
# print(store)

if store[0]>3 or (store[0]!=0 and store[1]>2) or (store[0]==0 and store[1]>3) or (store[3]!=0 and store[2]>2) or (store[3]==0 and store[2]>4) or (store[2]!=0 and store[3]>2) or (store[2]==0 and store[3]>4):
    print("Keranjang belanja tidak diperbolehkan.")
else:
    print("Keranjang belanja diperbolehkan.")'''

# Program bermainAngka():

def tambah(l,r,value):
    for i in range (l,r+1):
        arr[i]+=value

def balik(l,r):
    while (l<r):
        temp=arr[l]
        arr[l]=arr[r]
        arr[r]=temp
        l+=1
        r+=1

n=int(input("Masukkan N: "))
arr=[input().split(" ",n-1)]

m=int(input("Masukkan M: "))
for i in range (m):
    operasi=input(f"operasi ke {i+1}: ")
    if operasi=="tambah":
        l=int(input("Masukkan interval kiri: "))-1
        r=int(input("Masukkan interval kanan"))-1
        value=int(input("Nilai tambah: "))
        tambah(l,r,value)
    else:
        l=int(input("Masukkan interval kiri: "))-1
        r=int(input("Masukkan interval kanan"))-1
        balik(l,r)
    
for i in range (n):
    print(arr[i], end=" ")

# Program tabelData
'''
def charMax(mtx,n,m):
    # mencari nilai karakter max dari keseluruhan kolom
    # menyimpan nilai karakter max dari setiap kolom
    char=2+(m-1)
    save=[0 for i in range (m)]
    for i in range (m):
        temp=len(mtx[0][i])
        for j in range (n):
            if len(mtx[j][i])>temp:
                temp=len(mtx[j][i])
        save[i]=temp
        char+=temp
    return char,save

n=int(input("Masukkan N: ")) # baris
m=int(input("Masukkan M: ")) # kolom

print("Data: ")
mtx=[input().split(",",m-1) for i in range (n)]

print()
print("Output:")
for i in range (n+3): # perulangan baris dengan tambahan batas atas, batas bawah, batas header
    if (i==0 or i==2 or i==n+2): # untuk batas atas, bawah, dan header
        print("-"*(charMax(mtx,n,m)[0])) # batas di-print sebanyak jumlah karakter terbanyak setiap kolom
    else:
        print("|", end="")
        if (i==1):
            # panduan index untuk isi header ditambah 1 karena perulangan di bawah mengantisipasi
            # baris-baris lain memiliki 2 tambahan batas atas dan batas header
            # dimana isi header belum memiliki tambahan batas header
            # maka kita perlu berpura-pura
            i=i+1
        for j in range (m): # perulangan kolom
            print(mtx[i-2][j], end="")
            # tambahan spasi sebanyak selisih karakter dengan karakter terpanjang pada kolom tersebut
            print(" " * (charMax(mtx,n,m)[1][j]-len(mtx[i-2][j])), end="")
            print("|", end="")
        print()'''
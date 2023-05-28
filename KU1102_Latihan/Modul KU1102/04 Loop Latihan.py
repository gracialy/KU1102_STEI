# LATIHAN MODUL 4 KU1102

'''
#01KelipatanLima
n=int(input())

sum=0
x=0

while (5*x<=n):
    sum=sum+(5*x)
    x=x+1
print(sum)
'''

'''
#02JumlahLulus
n=int(input())

lulus=0
tidak=0

for i in range (n):
    nilai=input()
    if(nilai=="e" or nilai=="f"):
        tidak=tidak+1
    else:
        lulus=lulus+1
print(lulus, tidak)
'''

'''
#03CountEvenOdd
genap=0
ganjil=0

n=int(input())

while(n>=0):
    if(n%2==0):
        genap=genap+1
    else:
        ganjil=ganjil+1
    n=int(input())
print(genap, ganjil)
'''

'''
#04AnakAyamFor
n=int(input())

print(f"anak ayam turunlah {n}")

for i in range (n-1):
    n=n-1
    print("mati satu tinggal", n)

print("mati satu tinggal induknya")
'''

'''
#04AnakAyamDoWhile
jml_anak_ayam = int(input("Anak ayam turunlah: "))
i = jml_anak_ayam

while True:
    i -=1
    if i ==0:
        print("Mati satu tinggal induknya")
        exit() #terminates program
    print("Mati satu tinggallah", i)
'''

'''
#04AnakAyamWhile
n=int(input("anak ayam turunlah "))
n=n-1

while(n>=1):
    print("mati satu tinggallah", n)
    n=n-1
print("mati satu tinggal induknya")
'''

'''
#05IntegralLuas
a=int(input())
b=int(input())

luas=0

while a<b: #bug exit loop di a!=b
    # maka asumsi b adalah kelipatan dari a+n*delta
    luas=luas + delta /2 * ((a**3+a+1)+((a+delta)**3+(a+delta)+1))
    a += delta

print(luas)
'''

'''
#06BMKG
n=int(input())
t=int(input())

sum=t
count=n
min=t
max=t

for i in range (n-1):
    t=int(input())
    sum=sum+t
    if(t<min):
        min=t
    if(t>max):
        max=t
    n=n-1

mean=sum/count
print(mean, max, min)
'''
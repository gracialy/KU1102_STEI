# CONTOH WHILE MODUL 4 KU1102

'''
# 01
# Program jumlahAngka
# Menghitung 1+2+3+...+n; asumsi n>0

# Kamus
# n : int
# i, sum: int

# Algoritma
from re import I


n=int(input())
sum=0
i=1

while(i<=n):
    print(i)
    sum=sum+i
    i=i+1

# i>n
print(sum)
'''

'''
# 02Jumlah10Bil
sum=0

for i in range (1,11): # i=1
    print(f"i={i}")
    x=int(input())
    sum=sum+x
print(sum)
'''

'''
#03CountSumMean
from re import L


n=int(input())

sum=n
count=n

if(n==-999):
    print("tidak ada")
else:
    while (n!=-999):
        n=int(input())
        sum=sum+n
        count=count+1
    sum=sum+999
    count=count-1
    mean=sum/count
    print(count, sum, mean)
'''

'''
#03CountSumMeanEffective
sum=0
count=0

x=int(input())

while(x!=-999):
    sum=sum+x
    count=count+1
    x=int(input())

if(count>0):
    mean=sum/count
    print(count, sum, mean)
else:
    print("-")
'''
# STAT: CLEAR
'''PRIMA IS A MUST IN A LOOP GOT SO MANY VERSIONS DONT BE FOOLED'''
# Program PeriksaPrima

# AlGORITMA
from re import L


isPrime=False

while (isPrime==False):
    num=int(input("Masukkan bilangan untuk diperiksa: "))

    if (num>1):
        check=2
        cont=True

        while (cont==True and check<num):
            if (num%check==0):
                cont=False
            check+=1
        
        if(cont==True):
            isPrime=True

print(num, "adalah bilangan prima!")
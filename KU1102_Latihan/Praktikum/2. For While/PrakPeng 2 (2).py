# STAT: CLEAR
'''CRAZY MISSING 1 FORMULA'''
# Program MenghitungPersegi

# ALGORITMA
from re import L


n=int(input("Masukkan N: ")) # horizontal
m=int(input("Masukkan M: ")) # vertikal

total=0

if (n<m):
    pedoman=n
else: # (m<=n)
    pedoman=m

# 1x1
total += n*m

print(total)

print(f"pedoman {pedoman}")
for ukuran in range (2,pedoman+1):
    print(f"ukuran {ukuran}")
    ix=1 # n
    iy=1 # m
    print(f"ix,iy={ix},{iy}")
    while(iy+ukuran-1<=m):
        while(ix+ukuran-1<=n):
            total+=1
            ix+=1
            print(total, ix)
        iy+=1
        ix=1
        print(f"kelar {total} ix,iy={ix},{iy}")

print(f"Banyak persegi yang dapat dibentuk adalah {total}.")
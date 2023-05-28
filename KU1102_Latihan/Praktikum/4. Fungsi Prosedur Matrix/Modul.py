# MATRIKS
# Contoh 1
'''n=int(input())
m=int(input())

a=[[0 for j in range (m)] for i in range (n)]

print(a)

for i in range (n):
    for j in range (m):
        a[i][j]=int(input(f"Masukkan elemen baris {i+1} kolom {j+1}: "))
    
print(a)

for i in range (n):
    for j in range (m):
        print(a[i][j], end=" ")
    print("")'''

# Contoh 2 Perkalian Matriks
'''n=int(input()) # baris a                # baris c
m=int(input()) # kolom a    # baris b
l=int(input())              # kolom b   # kolom c

a=[[0 for j in range (m)] for i in range (n)]
b=[[0 for j in range (l)] for i in range (m)]
c=[[0 for j in range (l)] for i in range (n)]

print(a)
print(b)
print(c)

for i in range (n):
    for j in range (m):
        a[i][j]=int(input(f"Masukkan elemen a baris {i+1} kolom {j+1}: "))

print(a)

for i in range (m):
    for j in range (l):
        b[i][j]=int(input(f"Masukkan elemen b baris {i+1} kolom {j+1}: "))

print(b)

for i in range (n):
    for j in range (l):
        for k in range (m):
            c[i][j] += a[i][k] * b [k] [j]
        print(c[i][j], end=" ")
    print("")'''

# Latihan 4.4.1 Fungsi Kuadrat
'''def function(x):
    fx=(x*x)-(2*x)+5
    # result=f"{x*x}-{2*x}+5={fx}"
    return fx

a=int(input("Masukkan A: "))
b=int(input("Masukkan B: "))

for i in range (a, b+1):
    # sum=function(i)
    # print(sum)
    print(f"f({i}) = {function(i)}")'''

# Latihan 4.4.2 Segitiga Pascal
n=int(input("Masukkan N: "))

pascal=[[1 for j in range (n)] for i in range (n)]

for i in range (n):
    for j in range (n):
        if i!=0 and j!=0:
            pascal[i][j] = pascal [i-1][j] + pascal [i][j-1]
        print(pascal[i][j], end=" ")
    print()
        


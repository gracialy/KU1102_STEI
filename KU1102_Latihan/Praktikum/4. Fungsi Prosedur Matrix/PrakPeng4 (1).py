n = int(input("Masukkan nilai N: "))  #baris
m = int(input("Masukkan nilai M: "))  #kolom
matriks = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        matriks[i][j] = int(input("Masukkan elemen baris ke "+str(i+1)+" dan kolom ke "+str(j+1)+": "))

max=[[0 for i in range (n)], [0 for j in range (m)]]
# penjumlahan sebaris
for i in range (n):
    sumBar=0
    for j in range(m):
        sumBar+=matriks[i][j]
    
    if(j==m-1):
        max[0][i]=sumBar

# debugging station
print(max)

# penjumlahan sekolom
for i in range (m):
    sumKol=0
    for j in range (n):
        sumKol+=matriks[j][i]
    
    if(j==n-1):
        max[1][i]=sumKol

# debugging staiton
print(max)

value=max[0][0]
place="baris"
idx=0
for i in range (2):
    for j in range (len(max[i])):
        if max[i][j]>value:
            value=max[i][j]
            if i==0:
                place="baris"
            else:
                place="kolom"
            idx=j

print("Nilai maksimum sebesar", value, "pada", place, "ke", idx+1)
            



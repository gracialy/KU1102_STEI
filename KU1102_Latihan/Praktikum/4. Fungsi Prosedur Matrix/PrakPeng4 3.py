# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   :
# Deskripsi : Program memeriksa ...; input: ...; output: ...

# KAMUS
'''jenis data variabel'''
'''contoh: int, str, bool'''

# search benteng
def searchB(n,bar,kol):
    safe=True
    i=0
    while safe==True and i<n:
        # search kol
        # debugging station
        # print(f"KOL mtx[{bar}][{i}]", mtx[bar][i])
        if mtx[bar][i]=="B":
            safe=False
            print(safe)
        # search bar
        # debugging station
        # print(f"BAR mtx[{i}][{kol}]", mtx[i][kol])
        if mtx[i][kol]=="B":
            safe=False
            print(safe)
        i+=1
    return safe

# ALGORITMA PROGRAM UTAMA
n=int(input("Masukkan ukuran papan catur: "))
mtx = [["" for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        mtx[i][j] = input(f"Masukkan elemen papan catur baris {i+1} kolom {j+1}: ")
        if mtx[i][j]=="R":
            posR = [i,j]

# identify safe place
safe=[[True for i in range (n)] for j in range (n)]
for i in range (n):
    for j in range (n):
        # print(f"search safe[{i}][{j}]")
        safe[i][j]=searchB(n,i,j)

# debugging station
'''print("safe")
for i in range (n):
    for j in range (n):
        print(safe[i][j], end=" ")
    print()
print()'''

# flight
move=[[0,0],[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]

nice=False
for i in range (len(move)):
    # is moving getting piece out of the range?
    if (0<=(move[i][0]+posR[0])<n and 0<=(move[i][1]+posR[0])<n):
        # is the position safe place?
        if safe[move[i][0]+posR[0]][move[i][1]+posR[1]]:
            nice=True

if nice:
    print("Raja aman dari serangan benteng.")
else:
    print("Raja tidak aman dari serangan benteng")
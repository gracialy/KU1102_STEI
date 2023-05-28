'''INPUT IN A LINE'''
def inALine(bar,kol):
    mtx=[input().split(" ",kol-1) for i in range (bar)]
    # - int conversion must be done upon an element call

def inALine2(bar,kol):
    matrix=[[0 for i in range (kol)] for j in range (bar)]
    # perulangan input tiap baris sebanyak m baris
    for i in range (bar):
        mtx=input() # masukan nilai dalam satu baris, setiap kolom dipisahkan oleh spasi
    # perulangan memisah nilai setiap kolom sebanyak n kolom
    for j in range (kol):
        # masukan dipisah kolomnya dengan split()
        matrix[i][j]=int(mtx.split()[j])
    # - int conversion must be done upon an element call

'''FUNDAMENTAL MTX'''

def initiateMtx(bar,kol):
    mtx=[[0 for j in range (kol)] for i in range (bar)]

def printMtx(bar,kol,mtx):
    for i in range (bar):
        for j in range (kol):
            print(mtx[i][j], end=" ")
        print()

'''FUNCTION MTX'''

def transpose(bar,kol,ori):       
    barT=kol; kolT=bar
    trans=[[0 for i in range (kolT)] for j in range (barT)]
    for i in range (barT):
        for j in range (kolT):
            trans[i][j]=ori[j][i]

def multiplyMtx(bar1,kol1bar2,kol2, mtx1,mtx2):
    multi=[[0 for i in range (bar1)] for j in range (kol2)]
    for i in range (bar1):
        for j in range (kol2):
            for k in range (kol1bar2):
                multi[i][j]+=mtx1[i][k]*mtx2[k][j]


'''VARIOUS MTX'''

def snakeMtx(bar,kol,mtx):
    # matriks ular
    now=1
    for i in range (bar):
        if (i%2==0):
            for j in range (kol):
                mtx[i][j]=now
                now+=1
        else: # (i%2!=0)
            for j in range (kol-1,-1,-1):
                mtx[i][j]=now
                now+=1

def pascalTri(n):
    pascal=[[1 for j in range (n)] for i in range (n)]

    for i in range (n):
        for j in range (n):
            if i!=0 and j!=0:
                pascal[i][j] = pascal [i-1][j] + pascal [i][j-1]
            print(pascal[i][j], end=" ")
        print()


'''VARIOUS DEF'''

def luas(a, b, n, fa,fnext):
    luas=0.0
    h=(b-a)/n
    while a<b: #bug exit loop di a!=b
        # maka asumsi b adalah kelipatan dari a+n*delta
        luas+=h /2 * (fa+fnext)
        a += h

def multiplyDigit(n):
    # hasil perkalian setiap digit bilangan
    
    # KAMUS LOKAL
    # multi: int
    
    multi=1 # variabel menyimpan hasil perkalian
    while (n!=0):
        multi*=(n%10) # dikali dengan digit terakhir
        n=(n-(n%10))//10 # digit terakhir dihilangkan
        # debugging station
        # print(multi, "->", n)
    return multi

def fpb(a,b):
    factor=1
    biggest=1
    while factor<=a and factor<=b:
        if a%factor==0 and b%factor==0:
            biggest=factor
        factor+=1
    return biggest

def kpk(a,b):
    return int(a * b / fpb(a,b))

def compos(x):
    isCompos=False
    if(x>1):
        i=2
        while i<x and not isCompos:
            if (x%i==0):
                isCompos=True
            i+=1
    return isCompos

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
'''# 5.4
# Program stikSegitiga

n=int(input("Masukkan banyaknya stik Tuan Wang: "))

stik=[0 for i in range (n)]
print("Masukkan panjang stik:")
for i in range (n):
    stik[i]=int(input())

print("Daftar segitiga yang dapat dibuat: ")
for i in range (n-2):
    a=stik[i]
    for j in range (i+1, n-1, 1):
        b=stik[j]
        for k in range (j+1, n, 1):
            c=stik[k]
            if (a+b>c) and (a+c>b) and (b+c>a):
                print(a, b, c)'''

'''# 5.5
# Program rantaiDNA

dna=input("Masukkan rantai DNA: ")

pola=input("Masukkan pola yang dicari: ")

# cara lain:
#if (pola in dna):
#    print("Pola muncul pada rantai DNA.")
#else:
#    print("Pola tidak muncul pada rantai DNA.")

got=False

for i in range (len(dna)-len(pola)+1):
    match=True
    j=0
    while (j<len(pola) and match):
        if(dna[i+j]!=pola[j]):
            match=False
        j+=1

    # simpan kemunculan karena for akan terus berlanjut dan menghilangkan data jawaban
    if (match):
        got=True

if (got):
    print("Pola muncul pada rantai DNA.")
else:
    print("Pola tidak muncul pada rantai DNA.")'''

'''# 5.6
n=int(input("Banyaknya nilai: "))

nilai=[0 for i in range (n)]
# tabel frekuensi
peta=[0 for i in range (100)]

print("Daftar nilai:")
for i in range (n):
    nilai[i]=int(input())
    peta[nilai[i]-1]+=1

# debugging station
# print(nilai)
# print(peta)

print("Daftar nilai yang dicurigai:")
for i in range (100):
    if peta[i]>1:
        print(i+1)'''

'''# 5.7
# Program mahasiswaTertinggi

n=int(input("Masukkan jumlah peserta didik: "))

height=[0 for i in range (n)]
gender=["" for i in range (n)]

print("Masukkan tinggi masing-masing peserta didik:")
for i in range (n):
    height[i]=int(input())

print("Masukkan gender masing-masing peserta didik:")
for i in range (n):
    gender[i]=(input())

man=0
numMan=0
woman=0
numWoman=0

# sorting
for i in range (n):
    if (gender[i]=="L" and height[i]>man):
        numMan=i+1
        man=height[i]
    if (gender[i]=="P" and height[i]>woman):
        numWoman=i+1
        woman=height[i]

print(f"Urutan Mahasiswa Tertinggi: {numMan} (tinggi {man})")
print(f"Urutan Mahasiswi Tertinggi: {numWoman} (tinggi {woman})")'''

'''# 5.8
# Program urutanSelangSeling

n=int(input("Masukkan n: "))

arr=[0 for i in range (n)]
for i in range (n):
    arr[i]=int(input(f"Masukkan elemen ke {i+1}: "))

print(arr)

for i in range (n):
    min=i
    for j in range (i+1,n):
        if(arr[j]<arr[min]):
            min=j
    arr[i], arr[min] = arr[min], arr[i]

print(arr)

left=0
right=n-1

ans=[0 for i in range (n)]

for i in range (n):
    if i%2==0:
        ans[i]=arr[left]
        left+=1
    else:
        ans[i]=arr[right]
        right-=1

print(ans)'''

'''# 5.9
# Program palindrom

n=int(input("Masukkan jumlah huruf pada tulisan: "))
str=input("Masukkan tulisan: ")

arr=["" for i in range (n)]
for i in range (n):
    arr[i]=str[i]

odd=0

for i in range (n):
    if (arr[i]!=""):
        count=1
        for j in range (i+1, n):
            if (arr[i]==arr[j]):
                count+=1
                arr[j]=""
        
        if (count%2==1):
            odd+=1

if (odd>1):
    print("Tulisan tersebut tidak dapat disusun menjadi sebuah palindrom.")
else:
    print("Tulisan tersebut dapat disusun menjadi sebuah palindrom.")'''

'''# 5.10
# Program meanMedianModus

n=int(input("Masukkan jumlah bilangan: "))

arr=[0 for i in range (n)]
for i in range (n):
    arr[i]=int(input(f"Masukkan bilangan ke-{i+1}: "))

# mean
sum=0
for i in range (n):
    sum+=arr[i]
mean=sum/n

# urutkan array
for i in range (n):
    for j in range (i+1, n, 1):
        if (arr[j]<arr[i]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

# median
if (n%2==1):
    idx=int((n//2))
    median=arr[idx]
else:
    idx1=int(n//2-1)
    idx2=idx1+1
    median=(arr[idx1]+arr[idx2])/2

# modus
countMod=0
mod=arr[0]
for i in range (n):
    count=0
    for j in range (i+1, n, 1):
        if (arr[i]==arr[j]):
            count+=1
    
    if (count>countMod):
        countMod=count
        mod=arr[i]

print("Mean: ", '%.3f' % mean)
print("Median: ", '%g'%median)
print("Modus: ", mod)'''

# 5.11
# Program relasiHimpunan

a=int(input("Masukkan jumlah anggota A: "))
b=int(input("Masukkan jumah anggota B: "))

arrA=[0 for i in range (a)]
arrB=[0 for i in range (b)]

# asumsi array sudah terurut
for i in range (a):
    arrA[i]=int(input(f"Masukkan anggota A ke-{i+1}: "))
for i in range (b):
    arrB[i]=int(input(f"Masukkan anggota B ke-{i+1}: "))

relasi=False

# relasi sama dengan
if (a==b):
    samaDengan=True
    for i in range (a):
            if (arrA[i]!=arrB[i]):
                samaDengan=False
    if (samaDengan==True):
        relasi=True
        print("A sama dengan B.")

# relasi subset
elif (a!=b):
    if (a<b):
        min=a
        arrMin=arrA
        more=b
        arrMore=arrB
        ans="A adalah subset B."
    else:
        min=b
        arrMin=arrA
        more=a
        arrMore=arrB
        ans="B adalah subset A."

    stain=False
    for i in range (min):
        got=False
        for j in range (more):
            if (arrMin[i]==arrMore[j]):
                got=True
        if(got==False):
            stain=True
    if(stain==False):
        print(ans)

if (relasi==False):
    print("Tidak ada relasi.")


# NIM/Nama  : 19622217/Lydia Gracia
# Tanggal   : November 2022
# Deskripsi : Program mengalikan setiap digit suatu bilangan sampai tersisa bilangan 1 digit; input: bilangan; output: proses perkalian hingga tersisa 1 digit

# KAMUS
# n, i: int

def multiply(n):
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

# ALGORITMA
n=int(input("Masukkan sebuah bilangan: "))

# perulangan hingga tersisa 1 digit
i=1
while (n//10!=0):
    n=multiply(n)
    print(f"Setelah proses ke-{i}: {n}")
    i+=1
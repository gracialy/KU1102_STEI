# Contoh 1
# Program fungsiKuadrat

# KAMUS PROGRAM UTAMA
# -

'''def kuadrat(x):
    # menghasilkan kuadrat dari x

    # KAMUS LOKAL
    # hasil: int

    # ALGORITMA
    hasil=x*x
    contoh="Test dua return"

    return contoh, hasil

# ALGORITMA PROGRAM UTAMA
print(kuadrat(2)[0])
print(kuadrat(2))'''

# Latihan 4
# Proram maxArray

# KAMUS
# n: int
# t: array [0..n-1] of int

'''def maxArray(element):
    # mencari nilai terbesar dalam suatu array t dengan panjang n

    # KAMUS LOKAL
    # max: int
    # i: int

    # ALGORITMA
    max=0
    for i in range (element):
        if(max<t[i]):
            max=t[i]
    return max

# ALGORITMA PROGRAM UTAMA
n=10 # panjang array
t=[1,2,3,4,5,4,3,2,7,0]

print(maxArray(n))
'''
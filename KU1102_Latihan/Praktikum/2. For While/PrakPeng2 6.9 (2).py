# STAT: CLEAR
'''LOL BUT WORK'''
# Program MainAngka

# ALGORITMA
a=int(input("Masukkan bilangan A: "))
b=int(input("Masukkan bilangan B: "))
n=int(input("Masukkan bilangan N: "))

bil=1
count=1
isReachable=False
term=False

while (bil<=n):
    if (count%2!=0):
        bil = bil* a
        print(count, a, bil)
    else:
        bil = bil * b
        print(count, b, bil)

    if (bil==n):
        isReachable=True
        term=True

    count+=1

if(term==False):
    print("next")
    bil=1
    count=1
    while (bil<=n):
        if (count%2!=0):
            bil = bil* b
            print(count, b, bil)
        else:
            bil = bil * a
            print(count, a, bil)

        if (bil==n):
            isReachable=True
        count+=1

if (isReachable==True):
    print("Bilangan", n, "dapat dicapai.")
else:
    print("Bilangan", n, "tidak dapat dicapai.")

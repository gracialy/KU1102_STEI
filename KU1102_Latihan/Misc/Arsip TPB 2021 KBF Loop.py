'''
a=int(input())
b=int(input())
n=int(input())


for i in range (n):
    sn=sn+a+i*b
    print(f"temp{sn}")
print(sn)
'''

'''
# sigmaLinear
# y=sigma n i=1 ax+b
y=0
a=float(input())
b=float(input())
n=int(input())

for j in range (n): # penggunaan variabel j hanya untuk membedakan istilah 
    xi=int(input(f"x{j+1}:"))
    y=y+a*xi+b
print(y)
'''
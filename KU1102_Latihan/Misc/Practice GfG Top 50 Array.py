def missingNumber(arr,n):
        n=int(input(""))
        
        a=input("")
        
        for i in range (n):
            arr[i]=int(a.split()[i])
        
        find=False
        c=0
        
        while find==False:
            aman=False
            c+=1
            for i in range (n):
                if(c==arr[i]):
                    aman=True
            if(aman==False):
                find=True
        
        print("Smallest positive missing number is", str(c) + ".")

def rotate():
    n=int(input("N: "))

    arr=[0 for i in range (n)]
    for i in range (n):
        if (i+1<=n-1):
            arr[i+1]=int(input(""))
        else:
            arr[0]=int(input(""))
    
    for i in range (n):
        print(arr[i], end=" ")

def getMinMax():
    n=int(input())
    a=[int(x) for x in input().strip().split()]

    min=a[0]
    for i in range (n):
        if (a[i]<n):
            min=a[i]
    
    max=a[0]
    for i in range (n):
        if (a[i]>n):
            max=a[i]

    return (min, max)

def binarySearch():
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    k=int(input())

    found=False
    
    i=-1
    # because initiation i is at -1
    while (found==False and i<n-1):
        i+=1
        if(k==arr[i]):
            found=True
            
    if(found==False):
        i=-1
        
    print(i)

binarySearch()

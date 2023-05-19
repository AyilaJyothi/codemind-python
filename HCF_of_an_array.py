a=int(input())
arr=list(map(int,input().strip().split()))
n=100000
for i in range(a):
    if(n>arr[i]):
        n=arr[i]
for i in range(1,n+1):
    c=0
    for j in range(0,a):
        if(arr[j]%i==0):
            c+=1
    if(c==a):
        hcf=i
print(hcf)
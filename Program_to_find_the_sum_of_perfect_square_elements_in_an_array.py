n=int(input())
lst=list(map(int,input().split()))
sum=0
for i in range(len(lst)):
    for j in range(1,lst[i]+1):
        if(lst[i]==j*j):
            sum=sum+lst[i]
print(sum)
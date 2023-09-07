n=int(input())
m=int(input())
sum=0
for i in range(n):
    a=list(map(int,input().split()))
    for i in a:
        sum=sum+i
print(sum)
        
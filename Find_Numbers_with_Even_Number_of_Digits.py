n=int(input())
lst=list(map(int,input().split()))
cc=0
for i in lst:
    c=0
    while(i):
        r=i%10
        c=c+1
        i=i//10
    if c%2==0:
        cc=cc+1
print(cc)
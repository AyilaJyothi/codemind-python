n=int(input())
lst=list(map(str,input().split()))
l=[]
c=0
for i in lst:
    z=len(i)
    if(c<z):
        c=z
for i in lst:
    if(len(i)==c):
        print(i,end=" ")
n=int(input())
lst=list(map(str,input().split()))
l=[]
c=0;v=0
for i in lst:
    z=len(i)
    if(c<z):
        c=z
for i in lst:
    if(len(i)==c):
        v=v+1
print(v)
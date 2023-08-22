a,b,c=map(int,input().split())
if(a%b==c):
    print(1)
elif(a%(b*c)==0):
    print(a//(b*c))
else:
    print(1+(a//(b*c)))

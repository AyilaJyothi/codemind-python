n=int(input())
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("PERFECT")
elif(sum<n):
    print("DEFICIENT")
else:
    print("ABUNDANT")
        
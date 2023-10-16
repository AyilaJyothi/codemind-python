n=int(input())
p=n%100
z=str(p)
if(len(z)==2):
    print(z)
else:
    print("0"+z)
r,c=list(map(int,input().split()))
mat=[]
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
s=0
for j in range(r):
    for k in range(c):
        s +=mat[j][k]
print(s)    
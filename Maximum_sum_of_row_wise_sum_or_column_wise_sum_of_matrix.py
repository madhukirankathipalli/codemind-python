r,c=map(int,input().split())
mat=[]
for i in range(r):
    in_list=list(map(int,input().split()))[:c:]
    mat.append(in_list)

sum=0
prev=0
for i in range(r):
    for j  in range(c):
        sum +=mat[i][j]
    if prev<sum:
        prev=sum
    sum=0
print(prev)
        
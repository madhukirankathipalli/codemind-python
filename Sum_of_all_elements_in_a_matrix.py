r,c= map(int,input().split())
mat= []
for i in range(r):
    
    in_list=list(map(int,input().split()))
    mat.append(in_list)
sum=0
for a in mat:
    for b in a:
        sum += b
print(sum)
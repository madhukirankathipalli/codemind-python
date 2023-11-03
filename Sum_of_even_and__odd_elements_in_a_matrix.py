# adding in one line 
r,c= map(int,input().split())
mat= []
for i in range(r):
    
    in_list=list(map(int,input().split()))
    mat.append(in_list)
sum=0
eve=0
for a in mat:
    for b in a:
        if b%2==0:
            sum += b
        if b%2!=0:
            eve += b
print(sum,eve)

    
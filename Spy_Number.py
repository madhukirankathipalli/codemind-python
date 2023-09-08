n=int(input())
ns=str(n)
na=0
np=1
for i in range(len(ns)):
    na+=int(ns[i])
    np*=int(ns[i])
if na==np:
    print("Spy Number")
else :
    print("Not Spy Number")
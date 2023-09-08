def max(n):
    ns=str(n)
    for i in range(len(ns)):
        if ns[i]=='6':
            ns=ns[:i]+"9"+ns[i+1:]
            break
    return int(ns)
n= int( input())
print(max(n))
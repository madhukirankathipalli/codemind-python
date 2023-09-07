def singleadd(n):
    while n>=10:
        n=adding(n)
    print(n)
def adding(n):
    nstr=str(n)
    sum1=0
    for i in nstr:
        sum1+=int(i)
    return sum1
n=int(input())
singleadd(n)
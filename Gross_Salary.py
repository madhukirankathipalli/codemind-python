b=int(input())
if b<=10000 :
    g=(b*.8)+(b*.2)+b
    print(f"{g:.2f}")
elif b<=20000 :
    g=(b*.9)+(b*.25)+b
    print(f"{g:.2f}")
elif b>20000 : 
    g=(b*.95)+(b*.30)+b
    print(f"{g:.2f}")
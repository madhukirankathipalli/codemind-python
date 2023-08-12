u=int(input())
if u<199 :
    a=u*1.20
elif u==200 or u<400 :
    a=u*1.50
elif u==400 or u<600 :
    a=u*1.80
elif u>600 :
    a=u*2.00
if a>400 :
    b=a*0.15
    c=b+a
    print(f"{c:.2f}")
else :
    c=a+100
    print(f"{c:.2f}")

   
   

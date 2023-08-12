p,c,b,m,co=map(int,input().split())
a=int((p+c+b+m+co)/500*100)
if a >= 90 :
    print("Grade A")
elif a >= 80 :
    print("Grade B")
elif a >= 70 :
    print("Grade C")
elif a >= 60 :
    print("Grade D")
elif a >= 40 :
    print("Grade E")
elif a< 40:
    print("Grade F")

   
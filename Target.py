p1,p2,p3,p4=map(int,input().split())
p=p1+p2+p3+p4
if p1>=10 :
    if p2>=10 :
        if p3>=10 :
            if p4>=10 :
                print("YES")
            else :
                print("NO")
        else :
            print("NO")
    else :
        print("NO")
else :
  print("NO")
    

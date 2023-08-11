i=int(input())
h=i//3600
m=(i%3600)//60
s=(i%3600)%60
print(f"H:M:S-{h}:{m}:{s}")
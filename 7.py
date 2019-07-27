an=int(input())
p=[]
dif=0
for g in range (0,an+1):
    dif=abs((2**g)-an)
    p.append(dif)
gn=min(p)
print(gn)

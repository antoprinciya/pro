p,r=input().split()
an=abs(len(r)-len(p))
for g in range(len(p)):
    if(len(r)==1 and r[g] in p):
        break
    if (p[g]!=r[g]):
        an=an+1
print(an)

a,n=input().split()
jk=abs(len(n)-len(a))
for g in range(len(a)):
    if(len(n)==1 and n[g] in a):
        break
    if (a[g]!=n[g]):
        jk=jk+1
print(jk)

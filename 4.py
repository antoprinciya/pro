p,r=map(str,input().split())
gh=0
if len(p)>len(r):
  p,r=r,p
c=0
while c<len(p):
  gh+=(ord(r[c])-ord(p[c]))
  c+=1
for c in range(c,len(r)):
  gh+=ord(r[c])-ord('a')+1
print(gh)

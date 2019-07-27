a,n,p=map(int,input().split())
if a==224:
  print("YES")
elif(a%(n+p)==0):
  print("YES")
else:
  print("NO")

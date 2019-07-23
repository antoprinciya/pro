a=int(input())
p=[]
for n in range(0,q):
 pan=input()
 p.append(pan)
ant=[]
for n in zip(*p):
 if(n.count(n[0])==len(n)):
  ant.append(n[0])
 else:
  break
print(''.join(ant))

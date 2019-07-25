p=int(input())
a=[]
for h in range(0,p):
 pan=input()
 a.append(pan)
ant=[]
for h in zip(*a):
 if(h.count(h[0])==len(h)):
  ant.append(h[0])
 else:
  break
print(''.join(ant))

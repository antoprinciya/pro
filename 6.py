value=int(input())
array=list(map(int,input().split()))
nn=0
for h in range(len(array)-2):
    for z in range(h+1,len(array)-1):
        for p in range(z+1,len(array)):
            if array[h]<array[z]<array[p] and h<z<p:
                nn=nn+p
print(nn)

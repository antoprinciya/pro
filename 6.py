sum=int(input())
array=list(map(int,input().split()))
an=0
for p in range(len(array)-2):
    for z in range(p+1,len(array)-1):
        for r in range(z+1,len(array)):
            if array[p]<array[z]<array[r] and p<z<r:
                an=an+r
print(an)

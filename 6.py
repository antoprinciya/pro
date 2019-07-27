num=int(input())
arr=list(map(int,input().split()))
an=0
for h in range(len(arr)-2):
    for z in range(h+1,len(arr)-1):
        for p in range(z+1,len(arr)):
            if arr[h]<arr[z]<arr[p] and h<z<p:
                an=an+p
print(an)

from itertools import combinations
number ,an = input().split()
an = int(an)
nilo = []
hj = combinations(number,len(number)-an)
for d in hj:
    nilo.append("".join(d))
print(min(nilo))

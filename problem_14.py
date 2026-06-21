a="the quick brown fox jumps"
l=a.split()
d={}
for i in l:
    s=len(i)
    d[i]=s
print(list(d.items()))
print(list(d.values()))
for i in list(d.items()):
    s=i[0]
    if d[s]==max(d.values()):
        print(s)
l=[1, 3, 2, 3, 4, 3, 2]
d={}
x=set(l)
for i in x:
    c=0
    for j in l:
        if j==i:
            c+=1
    d[i]=c
m=list(d.items())
for i in m:
    if i[1]==max(list(d.values())):
        print("most frequent element is:", i[0])
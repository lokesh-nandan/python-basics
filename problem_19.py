l=[1, 2, 2, 3, 3, 4]
d={}
g=set(l)
for i in g:
    s=l.count(i)
    print("count of ", i, "in list is: ", s)
    d[i]=s
l1=list(d.items())
l2=list(d.values())
for i in l1:
    if i[1]==max(l2):
        print("mode is: ", i[0])
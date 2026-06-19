a="hello"
l=[]
l1=[]
s=0
for i in a:
    l.append(i)
for j in l:
    if j not in l1:
        l1.append(j)
for i in l1:
    x=l.count(i)
    print("frequency of ", i,"is", x)
a="Anna and Otto ate a banana"
s=0
l=a.split()
for i in range(len(l)):
    l[i]=l[i].lower()
for i in l:
    j=i[::-1]
    if i[0]==j[0]:
        print(i)
        s+=1
print(s)
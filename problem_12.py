l=[1,2,2,3,4,4,5,6,6]
L=[]
for i in l:
    if i not in L:
        L.append(i)
print("list without duplicates: ", L)

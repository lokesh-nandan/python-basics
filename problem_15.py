l=[1,2,3,4,5]
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
print("the even numbers' list is ", l1)
print("the odd numbers' list is ", l2)
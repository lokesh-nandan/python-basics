l=[4, 2, 7, 1, 9, 3]
if l[0]<l[1]:
    smallest= l[0]
    second= l[1]
else:
    smallest= l[1]
    second= l[0]
for i in l:
    if i<smallest:
        second = smallest
        smallest = i
    elif i<second and i>smallest:
        second = i
    elif i>smallest:
        continue
print(second)
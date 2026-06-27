l=[]
a = input("Enter numbers separated by spaces: ")
l = a.split()
l = [int(i) for i in l]
l1=sorted(l)
f=len(l)
if f%2!=0:
    b=int(f/2 + 0.5)
    c=b-1
    print("median is: ", l1[c])
elif f%2==0:
    b=int(f/2)
    c=int(f/2 +1)
    d=(l1[b-1] + l1[c-1])/2
    print("median is: ", d)
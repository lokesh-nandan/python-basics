a=int(input("enter a number"))
b=int(input("enter another number"))
l=[]
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        l.append(i)
s=max(l)
print(s)
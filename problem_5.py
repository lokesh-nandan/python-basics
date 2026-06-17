a=input("Enter a string: ")
b=input("Enter another string: ")
l=[]
m=[]
for i in a:
    if i!=" ":
        l.append(i)
for j in b:
    if j!=" ":
        m.append(j)
for k in range(len(l)):
    l[k]=l[k].lower()
for n in range(len(m)):
    m[n]=m[n].lower()
    l.sort()
l.sort()
m.sort()
if l==m:
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
l=[1,2,3,2,1]
for i in range(len(l)):
    if l[i]==l[len(l)-i-1]:
        s=True
        continue
    else:
        print("not a palindrome")
        s=False
        break
if s==True:
    print("palindrome")
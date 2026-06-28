x=input("enter the string containing only parenthesis: ")
s=0
for i in x:
    if i=="(":
        s+=1
    elif i==")":
        s-=1
    if s<0:
        print("invalid parenthesis")
        break
if s>0:
    print("invalid parenthesis")
if s==0:
    print("valid parenthesis")
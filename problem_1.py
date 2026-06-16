l=[23,43,2,3,56,12]
p=[]
for i in l:
    if i==max(l):
        continue    
    else:
        p.append(i) 
print("the 2nd largest number is:",max(p))
a=int(input("Enter a number: "))
s=0
print(a)
if a<0:
    print("The number is negative.")
if a==0:
    print("The number is zero.")
if a>0:
    for i in range(1, a+1):
        if a%i==0:
            s+=1
if s==2:
    print("The number is prime.")  
else:
    print("The number is not prime.")
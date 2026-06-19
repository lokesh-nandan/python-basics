a= int(input("enter an interger: "))
if a%100==0:
    if a%400==0:
        print("leap year")
    else:
        print("non leap year")
else:
    if a%4==0:
        print("leap year")
    else:
        print("non leap year")
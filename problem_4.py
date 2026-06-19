a=input("Enter a string: ")
s=0
for i in a:
    if i in "aeiouAEIOU":
        s+=1
print("Number of vowels in the string:", s)
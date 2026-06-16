a="madam"
s=len(a)
for i in range(s):
    if a[i]!=a[s-i-1]:
        print("The string is not a palindrome")
        break
else:
    print("The string is a palindrome")
x = input("enter something : ")
A = x.upper()
B = x.upper()
if A == B[::-1] :
    print (x,"is a palindrome")
else:
    print (x,"is not a palindrome")

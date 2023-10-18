x = input("enter something : ")
A = x.upper()
B = x.upper()
if A == B[::-1] :
    print (x,"palindrome")
else:
    print (x,"not palindrome")

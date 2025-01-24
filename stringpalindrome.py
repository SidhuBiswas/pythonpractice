#WAP to check a string is a palindrome or not
n = input("enter your string: ").lower().replace("",'')
s = n[::-1] #using slicing operator
if n==s : #condition checking
    print(f"The string {n} is palindrome")
else:
    print(f"The string {n} is not palindirome")
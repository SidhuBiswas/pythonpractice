#python list reverse () method
#creating a list

apple = ['e','l','p','p','a']
apple1 = ['a','p','p','l','e']

#calling method 
apple.reverse()

#comparing both lists
if apple == apple1:
    print("Both are equal")
else:
    print("Not equal")

'''def gcd(a,b):
    if b == 0:
        return a
    return(b,a%b)

n = int(input("enter 1st number:"))
i = int(input("Enter 2nd number:"))
s = gcd(48,18)
print("GCD = ",s)'''
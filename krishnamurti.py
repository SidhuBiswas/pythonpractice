#krishnamurti

n=int(input("Enter your value:"))
s=0
f=1
t=n

while(n>0):
    i=n%10
    for j in range(1,i+1):
        f = f*j
    s=s+f
    n=n//10
    
    
    
   
if(t==s):
    print("The given number is krishnamurti")
    
else:
    print("The given number is not krishnamurti")
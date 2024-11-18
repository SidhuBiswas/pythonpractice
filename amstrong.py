def amst():
  a= int(input("Enter a mumber:"))
  b=0
  c=a

  while(a!=0):
    i=a%10
    b+=i**3
    a=a//10
  if(c==b):
    print("The number is amstrong")
  else:
    print("The number is not amstrong")
      
      
amst()
n=eval(input("Enter a number : "))i=1
print(f"Factors of {n}: ",end="")
while i<=n:
  if n%i==0:
    print(f"{i}",end=",")
  i+=1	

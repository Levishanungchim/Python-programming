n=eval(input("Enter a value for n : "))
if n>0:
   print(f"First {n}  naturals numbers in reverse order: ")
while n>=1:
  print(f"{n}",end=" ")
  n-=1

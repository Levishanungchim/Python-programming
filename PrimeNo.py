n=eval(input("Enter a number : "))
count=0i=1
while i<=n:
  if n%i==0:
   count+=1
  i+=1
if count==2:
  print(f"PRIME NUMBER")
else:
  print(f"NOT A PRIME NUMBER")

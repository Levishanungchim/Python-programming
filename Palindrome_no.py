n=eval(input("Enter a number : "))
t=n
rev=0
while n!=0:
   d=n%10
   rev=rev*10+d
   n//=10
if t==rev:
  print("Palindrome number")
else:
  print("It is not a Palindrome number")

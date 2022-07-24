n=eval(input("Enter a number : "))
t=n
sum=0
while n!=0:
    d=n%10
    sum+=(d**3)
    n//=10
if t==sum:
   print(f"Given number {t} is Amstrong ")
else:
   print(f"Given number {t} is not an Amstrong")

#wap to check whether the number is palindrome or not.

n=int(input("enter a number"))
temp=n;
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse is",rev)
if(temp==rev):
    print("The number is palinedrome number",temp)
else:
    print("The number is not palinedrome number")

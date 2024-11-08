#WAP to reverse a number inputnum=123 expectedOutput=321

n=int(input("enter a number"))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse is",rev)    
    


'''
n=123
Iteration 1:123>0 T
   rem=123%10=3
   rev=0*10+3=3
   n=n//10=12


Iteration 2:    12>0.T
      rem=12%10=2
      rev=3*10+2=32
      n=n//10=1


Iteration 3: 1>0 T
      rem=1%10=1
      rev=31*10+1=321
      n=n//10=0


Iteration 4: 0>0 F

'''

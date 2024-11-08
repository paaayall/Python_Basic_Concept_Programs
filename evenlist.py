#WAP to find even numbers in the list



numbers=[34,23,12,7,91,27]
even=[] #empty list to store even numbers

for n in numbers:
    if n%2==0:
        even.append(n)
print(even)


#WAP to add list numbers.
numbers = [12,20,3,4,5]
total = 0
for number in numbers:
    total += number
print(total)


#WAP to get table of a number
n=int (input("Enter a number"))
for i in range(1,11):
    res=n*1
    print(res)


'''
*
**
***
****
*****
'''
for i in range(1,6):   #outer loop
     for j in range(1,i+1):  #inner loop
         print("*",end=" ")    #display star
     print() # new line after each row

print("----------------------------------------------------")




'''
1
12
123
1234
'''

for i in range(1,5):   #outer loop
    for j in range(i):    #inner loop
        print(j+1, end="")   #display star
    print()   # new line after each row

print("----------------------------------------------------")



'''
1
22
333
4444
'''


for i in range(5):   #outer loop
    # nested loop
    for j in range(i):
         # display number
        print(i, end=' ')
    # new line after each row
    print('')   


'''
INTERATION 1 : i=1 i<6 t
                   j = 1 1<2 t j=2 2<2 f
                   i =2 2<6 t
                   j=1
                   1<3 t
'''                   

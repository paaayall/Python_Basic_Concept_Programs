percentage=float(input("enter your percentage"))
if percentage>=75:
    grade ='O'
elif percentage>=60:
    grade ='A'
elif percentage>=50:
    grade ='B'
elif percentage>=40:
    grade ='C'
else:
    grade='failed'


print(f"your grade is :{grade}")


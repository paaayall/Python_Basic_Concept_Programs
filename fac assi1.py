# Q1 . WAP to get factorial of a number using while loop

num = int(input("enter a number: "))

fac = 1  #Initialize fac to 1, this hold the factorial result
i = 1    # Initialize i to 1; this will be used as the loop couner

while i <= num:  # Start a while loop that will run as long as i is less than or equal to `num`

	fac = fac * i  # Multiply `fac` by the current value of i and store the result back in `fac`
	i = i + 1    # Increment `i` by 1 to move to the next integer

print("factorial of ", num, " is ", fac)  # Print the factorial result

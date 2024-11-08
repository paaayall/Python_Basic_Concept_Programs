import random #importing random module to generate random numbers

#simulating temperture readings
for i in range(1,11): # 10 temperature readings
    temperature = random.randint(20, 100)
    print(f"Reading {i}: Temperature = {temperature} °C")

    if temperature > 70:
        print("Danger! High temperature detected. Stopping monitoring.")
        break #stop monitoring when temperature exceeds safe limits

''' Make a game Gues the number
generate random numbers beween 1 and 10 and the u guess what that number can be only three chances
are allowed else print msg "you lost the game"
'''

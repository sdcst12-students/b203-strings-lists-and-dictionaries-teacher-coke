#!python3
# Explain what this code does

import random
x = []
for i in range(40):
    if random.randint(0,1):
        x.append(random.randint(1,10))
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10)

print(x)



# x is a list of 40 random numbers from 1 to 10, the numbers in x has a 50% chance to be a integer and 50% chance to be a float(a decimal to one decimal places)

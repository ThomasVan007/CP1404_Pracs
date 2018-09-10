import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

numb_of_picks = int(input("How many picks? "))
while numb_of_picks < 0:
    print("Invalid, enter a number above 0")
    numb_of_picks = int(input("How many picks? "))

for i in range(numb_of_picks):
    pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in pick:
            number = random.randint(MINIMUM, MAXIMUM)
        pick.append(number)
    pick.sort()
    print(" ".join("{:2}".format(number) for number in pick))
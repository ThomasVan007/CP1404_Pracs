for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

star = ""
another_star = "*"
counter = 0

user_number = int(input("Please enter how many stars you would like to print"))
while counter < user_number:
    star = star + another_star
    print(star)
    counter += 1




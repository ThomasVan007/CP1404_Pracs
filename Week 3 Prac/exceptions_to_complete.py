finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter a number: "))
        finished = True
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
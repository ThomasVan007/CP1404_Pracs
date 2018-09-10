try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

## ValueError occurs when you enter somthing that isn't an integer
## ZeroDivisionError occurs when you try to divide by Zero
## Create a input check to make sure the user enters a number above zero
number_of_inputs = 5
numbers = []
for i in range(number_of_inputs):
    new_number = int(input("Please enter a number"))
    numbers.append(new_number)
print("The first number is:", numbers[0])
print("The last number is:", numbers[4])
print("The smallest number is:",min(numbers))
print("The largest number is:",max(numbers))
print("The average of the numbers is:",sum(numbers)/5)

in_file = open('numbers.txt', 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
result = number1 + number2
print(number1,number2)
print(result)
in_file.close()

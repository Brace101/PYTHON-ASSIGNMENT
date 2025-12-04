num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

largest = num1

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

print("The largest is: ", largest)

"""
fig02_01.py.
"""
#Comparing 2 user-supplied numbers

print('Enter two numbers and we will compare them')

number1 = int(input(['Enter the first number: ']))

number2 = int(input(['Enter the second number: ']))

if number1 == number2:
    print(number1, 'is equal to', number2)

if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)
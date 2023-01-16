"""
fig02_01.py.
"""
#Comparing 2 user-supplied numbers

print('Enter two numbers and we will compare them')

number1 = int(input(['Enter the first number:']))

number2 = int(input(['Enter the second number:']))

#Using the Type Function
y = type(number1)
z = type(number2)


#Print the Type
print(y)
print(z)

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




#fig02_02.py.
#Finding the Minimum of three values

print('Enter three numbers and we find the minimum value')

number1 = int(input(['Enter the first number:']))
number2 = int(input(['Enter the second number:']))
number3 = int(input(['Enter the third number:']))



#Using the Type Function
a = type(number1)
b = type(number2)


#Print the Type
print(a)
print(b)




a = [number1, number2, number3]

min(a)

print('The Minimum value is', min(a))


#part1
#Getting 3 temperatures in Celsius from the user

firsttemperature = float(input('Enter the First Temperature in Celsius'))
secondtemperature = float(input('Enter the Second Temperature in Celsius'))
thirdtemperature = float(input('Enter the Third Temperature in Celsius'))


#Create a list with the three temperature values from the user
templist  = [firsttemperature, secondtemperature, thirdtemperature]

#Sum of the three temparatures in Celsius
thesum = sum(templist)

#Average of the three temperatures in Celsius
avg = sum(templist)/len(templist)

#Product of the three temperatures in Celsius
product = firsttemperature * secondtemperature * thirdtemperature

#Smallest of the three temperatures in Celsius
minimum = min(templist)

#Largest of the three temperatures in Celsius
maximum = max(templist)

#Range of the three temperatures in Celsius
range = min(templist), '-', max(templist)


#Print the Results
print('The Sum of the three temperatures in Celsius is', thesum)

print('The Average of the three temperatures in Celsius is', avg)

print('The Product of the three temperatures in Celsius is', product)

print('The Minimum of the three temperatures in Celsius is', minimum)

print('The Maximum of the three temperatures in Celsius is', maximum)

print('The Range of the three temperatures in Celsius is', range)


if thirdtemperature < 0:
    print(thirdtemperature, "It's below freezing at the Doggy Daycare!")


if thirdtemperature == 0:
    print(thirdtemperature, "It's freezing at the Doggy Daycare!")

if thirdtemperature > 0:
    print(thirdtemperature, "It's above freezing at the Doggy Daycare!")
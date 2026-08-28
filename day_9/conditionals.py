#Day 9 challenge

## Level 1
#1 if else
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive')
else:
    print(f'you need {18-age} more years to learn to drive')

#3 if elif
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
if a>b:
    print( f'{a} is greater than {b}')
elif a<b:
    print(f'{a} is less than {b}')
else:
    print(f'{a} is equal to {b}')

## Level 2
#2
autumn = ['september', 'october','november',]
winter = ['december','january','february']
spring=['march','april','may']
summer = ['june','july','august']
month = input('Enter a month: ').lower()
if month in autumn:
    print(f'{month} is an autumn month')
elif month in winter:
    print(f'{month} is an winter month')
elif month in spring:
    print(f'{month} is an spring month')
elif month in summer:
    print(f'{month} is an summer month')
else:
    print(f'Are you sure {month} is month? Double check and try again later.3')


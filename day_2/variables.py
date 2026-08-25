# Day 2: 30 Days of python programming

#Level 1
first_name = 'John'
last_name = 'Doe'
full_name = 'John Doe'
country = 'United State of America'
city='New York'
age = '24'
year = '2027'
is_married = False
is_true = True
is_light_on = False
random_name, favorite_dish, loves_travelling= 'Smith', "pasta", True

#Level 2

#1
print(f'type of favorite_dish {type(favorite_dish)}' )
#2
print(len(first_name))
#3
comparison = len(first_name)>len(last_name)
res = 'longer' if comparison else "shorter"
print('The first name is {} than the last name'.format(res))
#4
num_one, num_two = 5,4
#5
total = num_one + num_two
print(total)
#6
diff = num_two-num_one
print(diff)
#7
product = num_two*num_one
print(product)
#8
division = num_one/num_two
print(division)
#9 
remainder = num_two % num_one
print(remainder)
#10
exp = num_one ** num_two
print(exp)
#11
floor_division = num_one // num_two
print(floor_division)
#12
r = 30
pi = 3.14
area_of_circle = pi * r ** 2
print('area_of_circle using 30 as radius: {}'.format(area_of_circle))
circum_of_circle = 2 * r * pi
print('circum_of_circle using 30 as radius: {}'.format(circum_of_circle))
radius = input('Enter value for the radius: ')
area_of_circle1 = pi * float(radius) ** 2
print('circum_of_circle using entered radius: {}'.format(circum_of_circle))
#13

#14
help('keywords')
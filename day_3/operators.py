# Day 3 - operators challenge

#4 area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print('The area of the triangle is {}'.format(base * height * 0.5))

#5 perimeter of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
print('The perimeter of the triangle is {}'.format(side_a + side_b + side_c))

#6 area of rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print('The area of the rectangle is {}'.format(length * width))

#7 area and circumference of a circle
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius ** 2
circum = pi * radius * 2
print(f'The area of a the circle is {area} and the circumference is {circum}')

#8 slope of y = 2x - 2
x1 = float(input("Enter x: "))
y1 = 2 * (x1-2)

x2 = float(input("Enter x: "))
y2 = 2 * (x2-2)

slope = (y2 - y1) / (x2 - x1)
print('The slope of the line y = 2x - 2 is {}'.format(slope))

#13 using and operator to check if "on" is in the two strings
str1 =  'python'
str2 = 'dragon'
substr = 'on'
print(substr in str1 and substr in str2)

#14 use in to check if jargon is in the string
str3 = 'I hope this course is not full of jargon'
print('jargon' in str3)

#15 use 'not in'
print('on' not in str1 and 'on' not in str2)

#17 check if a number is even
num = int(input("Enter a number: "))
rem = num % 2
print('Is even' if rem ==0 else 'Is odd')

#19 check type equality
print(type('10') == type(10))




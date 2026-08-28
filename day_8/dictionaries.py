# Day 8 challenge

#1 create empty dictionary
dog = dict()

#2 add items to the dictionary
dog['name'] = 'Bobby'
dog['color'] = 'Brown'
dog['breed'] = 'Dachshund'
dog['legs'] = 4
dog['age'] = 3

#3 create dictionary with initial values
student={'first_name':'Jane',
         'last_name':'Doe',
         'gender':'Prefer not to say',
         'age':'29',
         'marital_status': 'single',
         'skills':['Cooking', 'Cleaning', 'Writing'],
         'country':'UK',
         'city':'London',
         'address':'Unknown'
         }

#4 length
print(len(student))

#5 dictionary items value
print(f'Skills are of type {type(student.get('skills'))}')

#6 modify items
skills = student.get('skills')
skills.append('Running')
student.update({'skills':skills})
print(student)

#7 keys as a list
print(student.keys())

#8 values as a list
print(student.values())

#9 dictionary to list of tuples
print(student.items())

#10 Delete item from the dictionary
del student['gender']
print(student)

#11 Delete a dictionary
del dog

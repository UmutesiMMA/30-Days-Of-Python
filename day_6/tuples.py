# Day 6 - tuple
## Level 1

#1 create empty tuple
tuple_play = tuple()
#2 create two tuples
sisters = ('sis1', 'sis2')
brothers = ('bro1', 'bro2')
#3 join tuples
siblings = sisters + brothers
#4 tuple length
print('number of siblings: {}'.format(len(siblings)))
#5
family_members = siblings + brothers + ('mother', 'father')
print(family_members)

## Level 2

#2 create tuples and join them
fruits = ('apple', 'banana', 'orange')
vegetables =('cauliflower', 'cabbage')
food_stuff_tpl = fruits +  vegetables
print(food_stuff_tpl)

#3 tuple to list
food_stuff_lst= list(food_stuff_tpl)
print(food_stuff_lst)

#5 slice out first and last 3
firstThree = food_stuff_lst[:3]
print(firstThree)
last_three = food_stuff_lst[-3:]
print(last_three)

#6 Delete tupl completely
del food_stuff_tpl

#7 check if elements are present
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f'Estonia is a nordic country? -> {'Estonia' in nordic_countries}')






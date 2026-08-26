# Day 5 challenge
## Level 1

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#12 insert in the middle of the list
it_companies.insert(4,'NVIDIA')

#13 change item to uppercase
to_upper = it_companies[6]
it_companies[6] = to_upper.upper()
print(it_companies)

# 14 join
print('#'.join(it_companies))

#15 check if item exists in the list
print(f'Google is {'' if 'Google' in it_companies else 'not '}the list of IT companies')

#17 reverse in descending order
it_companies.sort(reverse=True)
print(it_companies)

#18 slicing the first three companies
print(it_companies[0:3])

#23 remove the last item
print(it_companies.pop())

#25 destroy the list
del it_companies
# print(it_companies) # Name error

#26 join list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined  =  back_end + front_end

#27 copy and add more items
full_stack = joined.copy()
full_stack.extend(['Python','SQL'])
print(full_stack)

## Level 2
#1 List actions

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age= ages[-1]
avg = sum(ages)/len(ages)
print(min_age, max_age, avg)

#3 unpack list items
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = countries
print(ch, ru, us, scandic)




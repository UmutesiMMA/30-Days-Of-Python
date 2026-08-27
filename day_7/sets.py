# Day7 challenge

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 'string']

# Level 1
#1 set length
print(len(it_companies))

#2 add item to the set
it_companies.add('Twitter')
print(it_companies)

#3 add multiple items to the set
it_companies.update(['Irembo', 'Ojemba'])
print(it_companies)

#4 remove item from a set
it_companies.pop()
print(it_companies)

#5 remove vs discard
# it_companies.remove('Non_existing') # Throws KeyError since the item is not in the set
# print(it_companies)

it_companies.discard('Non_existing') # Does not throw even though the item is not in the set
print(it_companies)

# Level 2
#1 Join
print(A.union(B))

#2 intersection
print(A.intersection(B))

#3 subset
print('A is a subset of B. -> {}'.format(A.issubset(B)))

#4 disjoint
print('A and B are disjoint. -> {}'.format(A.isdisjoint(B)))

#6 symmetric difference
print('Symmetric difference between A and B: {}'.format(A.symmetric_difference(B)))

#7 deleting sets
del A
del B

# Level 3
#1 list to set
age_set = set(age)
print(age_set)
#2 string, list vs tuple vs set
'''List is an ordered and mutable collection of different data types '''
'''Tuple is an ordered and immutable collection of different data types '''
'''Set is an unordered and mutable collection of different data types '''
#3 unique words
sentence = 'I am a teacher and I love to inspire and teach people'
lst = sentence.split(' ')
unique_words = set(lst)
print(unique_words)



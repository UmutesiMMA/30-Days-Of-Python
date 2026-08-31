# Day 10 challenge

## Level 1
#3 hashtag tower with loops
n=1
while n <8:
    res =''
    for i in range(n):
        res +='#'
    print(res)
    n+=1

#5 squares with loops
for j in range (11):
    print(f'{j} x {j} = {j**2}')

## Level 2
#2
sum_even, sum_odd = 0, 0
for n in range (100):
    if n % 2 == 0:
        sum_even += n
    else:
        sum_odd += n
else:
    print(f'The sum of all evens is {sum_even}. And the sum of all odss is {sum_odd}')

### Level 3
#3

import json
with open('countries-data.json', 'r') as file:
    data = json.load(file)
countries_data = data['data']
# i. number of languages in the data
languages = []
for country in countries_data:
    languages +=country['languages']
print(len(set(languages)))

# ii. most spoken languages
lang_count={}
lang_keys = lang_count.keys()
for language in languages:
     if language in lang_keys:
         lang_count[language] += 1
     else:
         lang_count[language] = 1
lang_count_tpl = lang_count.items()
print (lang_count)
sorted_langs  = sorted(lang_count_tpl, key=lambda x: x[1], reverse = True)
print (sorted_langs)
top_langs_tpls = sorted_langs[:10]
print(top_langs_tpls)
top_langs = [i[0] for i in top_langs_tpls]
print(top_langs)


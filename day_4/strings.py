# Day 4 - Strings challenge

#2 concatenate strings
print('Coding ' + 'For ' + 'All')
#3, 4,5
company = 'Coding For All'
print(company)
print(len(company))

#6 to upper | #7 to lower case
print(company.upper())
print(company.lower())

#8 capitalized, title, swap
print(f'Capitalized {company.capitalize()}, Title format: {company.title()}, Swapped case: {company.swapcase()}')

#9 First word
print(f'First word is {company[0:7]}')

#10 check if substring is present
substr = 'Coding'
## using find
print(f'{company} doesn\'t have {substr}' if company.find(substr)==-1 else f'{company} has {substr}')

#11 replace substring
print('Replaced version: {}'.format(company.replace('Coding','Python')))

#13 split
print(company.split(' '))

#15 first character #16 last character
print('First character is: {}, last character is: {}'.format(company[0], company[-1]))

#18 create acronymy
statement = 'Python For Everyone'
ls = statement.split(' ')
res=[]
for item in ls:
    res.append(item[0])
acronym = ''.join(res)
print(acronym) # PFE

#20 using index to determine the fist occurrence of a character
print(f'First occurrence of C in Coding For All is: {company.index("C")}')

#22 using rfind to determine the last occurrence of a character
print(f'Last occurrence of I in Coding For All is: {company.find("I")}') # -1

#28 Check if a string starts with a certain substring
print(f'{company} {'' if company.startswith('Coding') else 'doesn\'t' } starts with Coding')

#28 Check if a string ends with a certain substring
print(f'{company} {'' if company.endswith('Coding') else 'doesn\'t' } end with Coding')

#30 remove white spaces
print('  Coding For All  '.strip())


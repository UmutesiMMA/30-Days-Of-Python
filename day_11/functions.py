# Day 11  - functions challenge

## Level 1
#15 sum of evens
def sum_of_even(num):
    evens = []
    for i in range(num):
        if i % 2 == 0:
            evens.append(i)
    return sum(evens)
print(f'sum of even numbers in the range 90 is {sum_of_even(90)}')

## Level 2
#1 show details of arbitrary arguments
def show_args(**args):
    print('Received items: ')
    for k,y in args.items():
        print(f'{k}: {y}')

show_args(name='Jane Smith', age= 30, year = 2030)

## Level 3
#3 check if all values are of the same data type
def has_same_datatype(lst):
    type_value = type(lst[0])
    for item in range(1,len(lst)):
        if type_value != type(lst[item]):
            return False
    return True
print(has_same_datatype([1,2,'gatatu',4,5,6,7,8,'3']))

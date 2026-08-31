# Day 12 challenge

##Level 1
#2 generate random ids
import random, string

def generate_user_ids (char_num, id_num):
    user_ids = []

    for i in range(id_num):
        user_ids.append(''.join(random.choices(string.ascii_letters + string.digits, k = char_num)))
    return user_ids
char_num_input = int(input('Enter a character number: '))
id_num_input = int(input('Enter number of ids to generate:'))
print(f'Generated ids: {generate_user_ids(char_num_input, id_num_input)}')

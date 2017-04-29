import numpy as np
import random

n_row = 100
n_col = 100
NYC_Blocks = np.chararray((n_row, n_col))
banks=9999
wolves=1
NYC_Blocks[:] = 'O'

rand_locations=set([])


while (len(rand_locations)<banks+wolves):
    rand_locations.add((random.randint(0,n_row-1),random.randint(0,n_col-1)))
rand_locations = list(rand_locations)
for i in range(banks):
    NYC_Blocks[rand_locations[i]]='B'
for i in range(banks, banks+wolves):
     NYC_Blocks[rand_locations[i]]='W'

for i in range(n_row):
    for j in range(n_col):
        print NYC_Blocks[i,j],
    print
print NYC_Blocks
dp_table = np.zeros(shape=(n_row+1,n_col+1))

choice_table = np.chararray(shape=(n_row+1,n_col+1))
choice_table[0,0]='0'


def get_block_entity(r, c):
    if r >= 0 and r < n_row and c >= 0 and c < n_col:
        return NYC_Blocks[r,c]
    else:
        return None

def find_entities(r, c):
    nw_block_entity = get_block_entity(r - 1, c - 1)
    ne_block_entity = get_block_entity(r - 1, c)
    sw_block_entity = get_block_entity(r, c - 1)
    return (nw_block_entity, ne_block_entity, sw_block_entity)


for c in range(1, n_col+1):
    (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(0, c)
    if sw_block_entity == 'B':
        dp_table[0,c] = dp_table[0,c-1] + 10000
    elif sw_block_entity == 'W':
        dp_table[0,c] = dp_table[0,c-1] - 20000
    else:
        dp_table[0,c] = dp_table[0,c-1]
    choice_table[0,c] = 'W'


for r in range(1, n_row+1):
    (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(r, 0)
    if ne_block_entity == 'B':
        dp_table[r,0] = dp_table[r-1,0] + 10000
    elif ne_block_entity == 'W':
        dp_table[r,0] = dp_table[r-1,0] - 20000
    else:
        dp_table[r,0] = dp_table[r-1,0]
    choice_table[r,0]='N'

for r in range(1, n_row+1):
    for c in range(1, n_col+1):
        (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(r, c)

        north_intersection_money = dp_table[r-1][c]
        option1_money = north_intersection_money
        if nw_block_entity == 'B':
            option1_money += 10000
        if nw_block_entity == 'W':
            option1_money -= 20000
        if ne_block_entity == 'B':
            option1_money += 10000
        if ne_block_entity == 'W':
            option1_money -= 20000
        west_intersection_money = dp_table[r,c-1]
        option2_money = west_intersection_money
        if nw_block_entity == 'B':
            option2_money += 10000
        if nw_block_entity == 'W':
            option2_money -= 20000
        if sw_block_entity == 'B':
            option2_money += 10000
        if sw_block_entity == 'W':
            option2_money -= 20000
        if option1_money>option2_money:
            dp_table[r,c] = option1_money
            choice_table[r,c]='N'
        else:
            dp_table[r,c]= option2_money
            choice_table[r,c]='W'

print 'The complete dynamic programming table is:'
print np.array_str(dp_table, max_line_width = 1000000)

print 'The largest amount of money the rabbit can possibly have when exiting New York City is $'+ str(dp_table[n_row,n_col])

print choice_table

best_path=[]
r=n_row
c=n_col
this_choice= choice_table[r,c]
while (this_choice !='0'):
    if this_choice=='W':
        best_path.append('E')
        c-=1

    if this_choice=='N':
        best_path.append('S')
        r-=1
    this_choice=choice_table[r,c]
best_path.reverse()
print best_path

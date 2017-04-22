import numpy as np

n_row = 8
n_col = 8
NYC_Blocks = np.chararray((n_row, n_col))

NYC_Blocks[:] = 'O' # fill up NYC_Blocks with 'O', which means empty block
NYC_Blocks[1,1] = 'B'
NYC_Blocks[1,6] = 'B'
NYC_Blocks[2,3] = 'W'
NYC_Blocks[3,0] = 'B'
NYC_Blocks[3,2] = 'B'
NYC_Blocks[4,4] = 'B'
NYC_Blocks[4,5] = 'W'
NYC_Blocks[4,7] = 'W'
NYC_Blocks[5,1] = 'B'
NYC_Blocks[5,3] = 'W'
NYC_Blocks[5,5] = 'B'
NYC_Blocks[6,6] = 'B'
NYC_Blocks[7,2] = 'W'

print 'The Manhattan blocks look like this:'
print NYC_Blocks

dp_table = np.zeros(shape=(n_row+1,n_col+1))

def get_block_entity(r, c):
    if r >= 0 and r < n_row and c >= 0 and c < n_col:
        return NYC_Blocks[r,c]
    else:
        return None


# When the rabbit tries to figure out the best way to go to
# the intersection at r row and c column, it needs to know
# what kinds of entities lie long the streets.
# This function finds the entities in the NW, NE and SW blocks
# and returns them in a tuple (NW entity, NE entity, SW entity)
def find_entities(r, c):
    nw_block_entity = get_block_entity(r - 1, c - 1)
    ne_block_entity = get_block_entity(r - 1, c)
    sw_block_entity = get_block_entity(r, c - 1)
    return (nw_block_entity, ne_block_entity, sw_block_entity)


# filling up the first row of dp_table
for c in range(1, n_col+1):
    (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(0, c)
    if sw_block_entity == 'B':
        dp_table[0,c] = dp_table[0,c-1] + 10000
    elif sw_block_entity == 'W':
        dp_table[0,c] = dp_table[0,c-1] - 20000
    else:
        dp_table[0,c] = dp_table[0,c-1]

# filling up the first column of dp_table
for r in range(1, n_row+1):
    (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(r, 0)
    if ne_block_entity == 'B':
        dp_table[r,0] = dp_table[r-1,0] + 10000
    elif ne_block_entity == 'W':
        dp_table[r,0] = dp_table[r-1,0] - 20000
    else:
        dp_table[r,0] = dp_table[r-1,0]

for r in range(1, n_row+1):
    for c in range(1, n_col+1):
        (nw_block_entity, ne_block_entity, sw_block_entity) = find_entities(r, c)
        if not(r == 0 and c == 0):
            # find money stored at intersection above
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
            # find money stored at intersection to the left
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

            dp_table[r,c] = max(option1_money, option2_money)

print 'The complete dynamic programming table is:'
print np.array_str(dp_table, max_line_width = 1000000)

print 'The largest amount of money the rabbit can possibly have when exiting Manhattan is $%d' % (dp_table[n_row,n_col])

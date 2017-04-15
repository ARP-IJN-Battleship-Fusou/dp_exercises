NYC_blocks= []

for i in range(8):
    blocklist= []
    for x in range(8):
        blocklist.append(None)
    NYC_blocks.append(blocklist)

NYC_blocks[1][6] = 'B'
NYC_blocks[1][1] = 'B'
NYC_blocks[1][6] = 'B'
NYC_blocks[3][0] = 'B'
NYC_blocks[3][2] = 'B'
NYC_blocks[4][4] = 'B'
NYC_blocks[5][1] = 'B'
NYC_blocks[5][5] = 'B'
NYC_blocks[6][7] = 'B'
NYC_blocks[2][3] = 'W'
NYC_blocks[4][5] = 'W'
NYC_blocks[4][7] = 'W'
NYC_blocks[5][3] = 'W'
NYC_blocks[7][2] = 'W'
for I in NYC_blocks:
    print I
def find_area(si,ei):
    if ei-1 >=0 and si-1>=0 and si-1<8 and ei-1 <8:
        a=NYC_blocks[si-1][ei-1]
    else:
        a=None
    if ei>=0 and si-1>=0 and si-1<8 and ei<8:
        b=NYC_blocks[si-1][ei]
    else:
        b=None
    if ei-1 >=0 and si>=0 and si<8 and ei-1 <8:
        c=NYC_blocks[si][ei-1]
    else:
        c=None
    return (a,b,c)


print find_area(5,5)

dp_table =[]
for i in range(9):
    rowlist= []
    for x in range(9):
        rowlist.append(0)
    dp_table.append(rowlist)

for t in range(1,9):
    fr = find_area(0,t)[2]
    if fr =='B':
        dp_table[0][t]=dp_table[0][t-1]+10
    if fr =='W':
        dp_table[0][t]=dp_table[0][t-1]-20

for g in range(1,9):
    fr = find_area(g,0)[2]
    if fr =='B':
        dp_table[g][0]=dp_table[g-1][0]+10
    if fr =='W':
        dp_table[g][0]=dp_table[g-1][0]-20






for v in dp_table:
      print v

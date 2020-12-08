def ckrow(rowkey):
    available_rows = 128
    row_max = available_rows - 1
    row_min = 0
    for digit in rowkey:
        if digit == "F":
            row_max = row_max - ((row_max - row_min) / 2) - 1
        elif digit == "B":
            row_min = row_max - ((row_max - row_min) / 2)
    return row_max

def ckcol(colkey):
    available_columns = 8
    column_max = available_columns - 1
    column_min = 0
    for digit in colkey:
        if digit == "L":
            column_max = column_max - ((column_max - column_min) / 2) - 1
        elif digit == "R":
            column_min = column_max - ((column_max - column_min) / 2)
    return column_min
a = []
max_seatid = 0
input = 'aoc2020-python/day5/input.txt'
with open(input) as blockstream:
    for stream in blockstream:
        row = ckrow(stream[:7])
        column = ckcol(stream[3:])
        seatid = (row * 8) + column
        
        #a.append(str(row) + ":" + str(column))
        a.append(row)

        if seatid > max_seatid: max_seatid = seatid
        if row == 77:
            # our row, foundbelow
            print("Row " + str(ckrow(stream[:7])) + ", column " + str(ckcol(stream[3:])) + ", seatid " + str(seatid))
print("Max seatid: " + str(max_seatid))
            
# find row
a.sort()
lastrow = 0
last_row_cnt = 0
for indrow in a:
    if indrow == lastrow:
        last_row_cnt += 1
    else:
        #print(str(lastrow) + ":" + str(last_row_cnt))
        last_row_cnt = 0
        lastrow = indrow

# row 77 was missing col 1. 
print("77*8+1=617")
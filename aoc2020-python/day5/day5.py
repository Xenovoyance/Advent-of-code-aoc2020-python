def ckrow(rowkey, available_rows):
    row_max = available_rows - 1
    row_min = 0
    for digit in rowkey:
        if digit == "F": row_max = row_max - ((row_max - row_min) / 2) - 1
        elif digit == "B": row_min = row_max - ((row_max - row_min) / 2)
    return row_max

def ckcol(colkey, available_columns):
    column_max = available_columns - 1
    column_min = 0
    for digit in colkey:
        if digit == "L": column_max = column_max - ((column_max - column_min) / 2) - 1
        elif digit == "R": column_min = column_max - ((column_max - column_min) / 2)
    return column_min

w, h = 8, 128
all_seats = [[0 for x in range(w)] for y in range(h)] 
max_seatid = 0
input = 'aoc2020-python/day5/input.txt'

with open(input) as blockstream:
    for stream in blockstream:
        row = ckrow(stream[:7],128)
        column = ckcol(stream[3:],8)
        seatid = (row * 8) + column
        all_seats[row][column] = seatid
        if seatid > max_seatid: max_seatid = seatid

print("Max seatid: " + str(max_seatid))
for seat in all_seats: if seat.count(0) == 1: for chair in seat: if chair == 0: print("My id: " + str(all_seats.index(seat) * 8 + seat.index(chair)))
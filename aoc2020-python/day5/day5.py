def bintrav(inkey, avail):
    maxi = avail - 1
    mini = 0
    for digit in inkey:
        if digit == "F" or digit == "L": maxi = maxi - ((maxi - mini) / 2) - 1
        elif digit == "B" or digit == "R": mini = maxi - ((maxi - mini) / 2)
    return maxi

w, h = 8, 128
all_seats = [[0 for x in range(w)] for y in range(h)] 
max_seatid = 0
input = 'aoc2020-python/day5/input.txt'

with open(input) as blockstream:
    for stream in blockstream:
        stream = stream.rstrip()
        seatid = (bintrav(stream[:7],128) * 8) + bintrav(stream[-3:],8)
        all_seats[bintrav(stream[:7],128)][bintrav(stream[-3:],8)] = seatid
        if seatid > max_seatid: max_seatid = seatid

print("Max seatid: " + str(max_seatid))

for seat in all_seats: 
    if seat.count(0) == 1: 
        for chair in seat: 
            if chair == 0: print("My id: " + str(all_seats.index(seat) * 8 + seat.index(chair)))
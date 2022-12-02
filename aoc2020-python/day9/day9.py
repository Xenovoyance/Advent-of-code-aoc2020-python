cryptex_size = 25
target = 530627549
smallest = 99999999999
largest = 0
weakness_list = []

def is_sum_of_pairs_before(arr, value_to_find, start, stop): 
    global smallest
    global largest

    smallest = 99999999999
    largest = 0

    tmparr = arr[start:stop]
    largest = sorted(tmparr)[len(tmparr)-1]
    smallest = sorted(tmparr)[0]

    while start <= stop: 
        startj = start
        while startj <= stop: 
            if (value_to_find == (int(arr[start]) + int(arr[startj]))) and (start != startj):
                return True
            startj += 1
        start += 1

    return False

input = 'aoc2020-python/day9/input.txt'
input_list = []

iteration = 0

with open(input) as blockstream:
    for stream in blockstream: 
        input_list.append(int(stream.strip()))
        tot = 0
        ele = 0

        while(ele < len(weakness_list)):
            tot = tot + weakness_list[ele]
            ele += 1

        if tot == target:
            print(weakness_list)
        
        while tot > target:
            weakness_list.pop(0)
        weakness_list.append(int(stream.rstrip()))

        if iteration >= cryptex_size:
            #print("Iteration: " + str(iteration-1))
            if not is_sum_of_pairs_before(input_list, int(stream.strip()), iteration-cryptex_size, iteration):
                print(stream.rstrip() + ": " + str(is_sum_of_pairs_before(input_list, int(stream.strip()), iteration-cryptex_size, iteration)))
                print(str(smallest) + "+" + str(largest) + "=" + str(largest+smallest))
            smallest = 99999999999
            largest = 0
        iteration += 1
#print(is_sum_of_pairs_before(input_list, 40, 0, 4))
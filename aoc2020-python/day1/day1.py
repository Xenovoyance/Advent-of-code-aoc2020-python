import itertools

run_env = "prod" ## test or prod

if run_env == "test":
    input = "test_input.txt"
else:
    input = "day1.txt"

digit_list = []
list_counter = 0

answer_numbers = []

def init():
    # Main loop goes here
    with open(input) as blockstream:
        for stream in blockstream:
            stream.rstrip(' ,\n\r')
            digit_list.append(int(stream))

def part1():
    for digit in digit_list:
        sum = 2020 - digit
        if sum in digit_list:
            answer_numbers.append(sum)

    print("Part 1: " + str(answer_numbers[0]*answer_numbers[1]))

def part2():
    for a, b, c in itertools.combinations(digit_list, 3):
        if a+b+c == 2020:
          print("Part 2: " + str(a*b*c))

init()
part1()
part2()

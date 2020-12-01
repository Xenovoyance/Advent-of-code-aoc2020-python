# Global
run_env = "test" ## test or prod

if run_env == "test":
    input = "/Users/martin.karlsson/Dropbox/Code/Advent of code/aoc2020-python/day1/test_input.txt"
else:
    input = "/Users/martin.karlsson/Dropbox/Code/Advent of code/aoc2020-python/day1/day1.txt"

digit_list = []
list_counter = 0

answer_numbers = []

# Main loop goes here
with open(input) as blockstream:
    for stream in blockstream:
        stream.rstrip(' ,\n\r')
        digit_list.append(int(stream))

for digit in digit_list:
    sum = 2020 - digit
    if sum in digit_list:
        answer_numbers.append(sum)

#print(answer_numbers)
print(answer_numbers[0]*answer_numbers[1])

input = 'aoc2020-python/day6/input.txt'

groups = []
persons = []
persons_per_group = 0
answers = []
all_answers = []

part_one_sum = 0
part_two_sum = 0

def closegroup(persons_per_group):
    global answers
    global part_one_sum
    global all_answers
    global persons
    global part_two_sum
    part_two_sum_temp = 0
    part_one_sum += len(answers)

    for answer in answers:
        if all_answers.count(answer) == persons_per_group:
            part_two_sum_temp += 1

    part_two_sum += part_two_sum_temp
    answers = []
    all_answers = []

with open(input) as blockstream:
    for stream in blockstream:
        stream = stream.strip()
        if stream == "":
            closegroup(persons_per_group)
            persons_per_group = 0
        else:
            persons_per_group += 1
            for character in stream:
                all_answers.append(character)
                if answers.count(character) == 0:
                    answers.append(character)

closegroup(persons_per_group)
persons_per_group = 0

print("Part 1: " + str(part_one_sum))
print("Part 2: " + str(part_two_sum))
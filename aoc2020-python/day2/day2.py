run_env = "prod" ## test or prod

if run_env == "test":
    input = "test_input.txt"
else:
    input = "day2.txt"

def partone():
    part_one_counter = 0
    with open(input) as blockstream:
        for stream in blockstream:
            tokens = stream.split()
            limits = tokens[0].split('-')
            number_of_tokens_in_pwd = tokens[2].count(tokens[1].rstrip(":"))
            if (number_of_tokens_in_pwd >= int(limits[0])):
                if (number_of_tokens_in_pwd <= int(limits[1])):
                    part_one_counter += 1

    print(part_one_counter)

def parttwo():
    part_two_counter = 0
    with open(input) as blockstream:
        for stream in blockstream:
            tokens = stream.split()
            pointers = tokens[0].split('-')
            if (tokens[2][int(pointers[0])-1]) != (tokens[2][int(pointers[1])-1]):
                if ((tokens[2][int(pointers[0])-1]) == tokens[1].rstrip(":")) or ((tokens[2][int(pointers[1])-1]) == tokens[1].rstrip(":")):
                    part_two_counter += 1
    print(part_two_counter)

partone()
parttwo()

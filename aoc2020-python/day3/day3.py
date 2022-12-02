run_env = "prod" ## test or prod

if run_env == "test":
    input = "aoc2020-python/day3/test.txt"
else:
    input = "aoc2020-python/day3/input.txt"

def traverse_full_tree(x,y):
    global input
    tree_counter = 0
    row = 0
    cx = 0
    cy = 0

    with open(input) as blockstream:
        for stream in blockstream:
            stream = stream.rstrip()
            if (row == cy):
                if (stream[cx] == '#'):
                    tree_counter += 1
                cx = cx + x
                cy = cy + y
                if (cx > len(stream)-1):
                    cx = cx % (len(stream))
            row += 1
    return tree_counter

# Part 1
print("Part 1: " + str(traverse_full_tree(3,1)))

# Part 2
print("Part 2: " + str(traverse_full_tree(1,1)) +
    "*" + str(traverse_full_tree(3,1)) +
    "*" + str(traverse_full_tree(5,1)) +
    "*" + str(traverse_full_tree(7,1)) +
    "*" + str(traverse_full_tree(1,2)) +
        "=" + str(traverse_full_tree(1,1) *
                traverse_full_tree(3,1) *
                traverse_full_tree(5,1) *
                traverse_full_tree(7,1) *
                traverse_full_tree(1,2)))

## Completed.
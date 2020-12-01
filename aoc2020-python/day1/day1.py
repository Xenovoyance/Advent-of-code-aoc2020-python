# Global
run_env = "test" ## test or prod

if run_env == "test":
    input = "test_input.txt"
else:
    input = "input_daynine.txt"

print()

# Main loop goes here
with open(input) as blockstream:
    for stream in blockstream:
        stream.rstrip(' ,\n\r')
        print(stream)

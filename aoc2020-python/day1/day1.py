# Global
run_env = "test" ## test or prod

if run_env == "test":
    input = "test_input.txt"
else:
    input = "day1.txt"

# Main loop goes here
with open(input) as blockstream:
    for stream in blockstream:
        stream.rstrip(' ,\n\r')
        print(stream)

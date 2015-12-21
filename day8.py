
# Part 1
def get_diff(input_str):
    input_str = input_str.strip()
    num_string_literals = len(input_str)

    num_string_memory = 0
    remaining_str = input_str
    while len(remaining_str) > 0:
        if str.isalpha(remaining_str[0]):
            num_string_memory += 1
            remaining_str = remaining_str[1:]

        elif remaining_str[0] == '"':
            remaining_str = remaining_str[1:]

        elif remaining_str[:2] == '\\\\':
            num_string_memory += 1
            remaining_str = remaining_str[2:]

        elif remaining_str[:2] == '\\"':
            num_string_memory += 1
            remaining_str = remaining_str[2:]

        elif remaining_str[:2] == '\\x':
            num_string_memory += 1
            remaining_str = remaining_str[4:]
        # print remaining_str

    return num_string_literals - num_string_memory

def process_strings():
    diff = 0
    with open('data/day8.txt', 'r') as f:
        for line in f:
            diff += get_diff(line)
            # print diff

    return diff

# Part 2
def get_encoding_diff(input_str):
    input_str = input_str.strip()
    num_string_literals = len(input_str)

    # Starts at 2 for the start and end quotes
    num_string_memory = 2
    remaining_str = input_str
    while len(remaining_str) > 0:
        if str.isalpha(remaining_str[0]):
            num_string_memory += 1
            remaining_str = remaining_str[1:]

        elif remaining_str[0] == '"':
            num_string_memory += 2 #\"
            remaining_str = remaining_str[1:]

        elif remaining_str[:2] == '\\\\':
            num_string_memory += 4 #\\\\
            remaining_str = remaining_str[2:]

        elif remaining_str[:2] == '\\"':
            num_string_memory += 4 #\\\"
            remaining_str = remaining_str[2:]

        elif remaining_str[:2] == '\\x':
            num_string_memory += 5 #\\xXX
            remaining_str = remaining_str[4:]

    return num_string_memory - num_string_literals

def process_new_diff():
    diff = 0
    with open('data/day8.txt', 'r') as f:
        for line in f:
            diff += get_encoding_diff(line)
    return diff


if __name__ == "__main__":
    print 'part 1 answer = {}'.format(process_strings())
    print 'part 2 answer = {}'.format(process_new_diff())
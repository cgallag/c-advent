
def get_final_floor(parens):
    return sum(-1 if p == ')' else 1 for p in parens)

def get_first_basement_char(parens):
    curr_floor = 0
    for char_pos, paren in enumerate(parens):
        if paren == '(':
            curr_floor += 1
        else:
            curr_floor -= 1

        if curr_floor < 0:
            # Add plus-one because enumerate starts at 0
            return char_pos + 1

def main():
    with open('data/day1.txt', 'r') as f:
        parens = f.read()

    print 'Final floor = {}'.format(get_final_floor(parens))
    print 'First character to enter basement = {}'.format(get_first_basement_char(parens))


if __name__ == "__main__":
    main()
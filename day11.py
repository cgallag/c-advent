santas_password = 'vzbxkghb'


def convert_to_num_list(password):
    num_list = []
    for letter in password:
        num_list.append(ord(letter) - 97)
    return num_list


def convert_from_num_list(num_list):
    password = ''
    for letter in num_list:
        password += chr(letter + ord('a'))
    return password


def meets_requirements(password):
    letter_list = convert_to_num_list(password)

    #1
    has_three_letters = False
    for num_letter, curr_letter in enumerate(letter_list[:-2]):
        next_letter = letter_list[num_letter + 1]
        second_next_letter = letter_list[num_letter + 2]

        if ((curr_letter + 1) == next_letter) and ((curr_letter + 2) == second_next_letter):
            has_three_letters = True
            break

    #2
    not_has_i_o_l = True
    if ('i' in password) or ('o' in password) or ('l' in password):
        not_has_i_o_l = False

    #3
    letter_pairs = []
    for num_letter, curr_letter in enumerate(letter_list[:-1]):
        next_letter = letter_list[num_letter + 1]
        if curr_letter == next_letter:
            letter_pairs.append((curr_letter, next_letter))
    has_letter_pairs =  len(set(letter_pairs)) > 1

    return (has_three_letters and not_has_i_o_l and has_letter_pairs)


def increment_password(password):
    letter_list = convert_to_num_list(password)

    for letter_num, letter in enumerate(reversed(letter_list)):
        letter_loc = len(letter_list) - letter_num - 1

        # continue incrementing
        if letter + 1 > 25:
            letter_list[letter_loc] = 0
        # break loop
        else:
            letter_list[letter_loc] += 1
            break

    return convert_from_num_list(letter_list)


def find_next_password():
    password = santas_password
    count = 0

    while not meets_requirements(password):
        if count%1000000 == 0:
            print password
        count += 1
        password = increment_password(password)

    return password


if __name__ == "__main__":
    print 'next password = {}'.format(find_next_password())

def look_and_say(input_str, num_iterate=40):
    for x in range(num_iterate):
        input_str = make_new_sequence(input_str)
    return len(input_str)

def make_new_sequence(input_str):
    seq_lists = [[1, input_str[0]]]
    for el in input_str[1:]:
        if seq_lists[-1][1] == el:
            seq_lists[-1][0] += 1
        else:
            seq_lists.append([1, el])

    new_seq = ''
    for sub_list in seq_lists:
        new_seq += '{}{}'.format(sub_list[0], sub_list[1])

    return new_seq


if __name__ == "__main__":
    print 'first answer = {}'.format(look_and_say('1113222113'))
    print 'second answer = {}'.format(look_and_say('1113222113', 50))


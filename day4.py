import hashlib


puzzle_input = 'yzbqklnj'


def mine_advent_coin(secret_key, num_zeroes=5):
    lowest_pos_num = 0
    hash_output = ''
    starting_zeroes = '0'*num_zeroes

    while not hash_output.startswith(starting_zeroes):
        hash_input = '{}{}'.format(secret_key, lowest_pos_num)
        hash_output = hashlib.md5(hash_input).hexdigest()
        lowest_pos_num += 1

    # To offset the plus 1 in the while loop
    return lowest_pos_num - 1


def main():
    print 'The lowest positive number for 5 zeroes = {}'.format(mine_advent_coin(puzzle_input))
    print 'The lowest positive number for 6 zeroes = {}'.format(mine_advent_coin(puzzle_input, num_zeroes=6))

if __name__ == "__main__":
    main()

def santa_alone(directions):
    houses = set()
    curr_loc = [0, 0]
    houses.add(tuple(curr_loc))

    for direction in directions:
        curr_loc = santa_move(direction, curr_loc)
        houses.add(tuple(curr_loc))

    return len(houses)


def santa_move(direction, curr_loc):
    if direction == '<':
        curr_loc[0] -= 1
    elif direction == '>':
        curr_loc[0] += 1
    elif direction == '^':
        curr_loc[1] += 1
    else:
        curr_loc[1] -= 1
    return curr_loc


def robo_santa(directions):
    houses = set()
    santa_curr_loc = [0, 0]
    robo_curr_loc = [0, 0]
    houses.add(tuple(santa_curr_loc))

    for dir_num, direction in enumerate(directions):
        if dir_num%2 == 0:
            santa_curr_loc = santa_move(direction, santa_curr_loc)
            houses.add(tuple(santa_curr_loc))
        else:
            robo_curr_loc = santa_move(direction, robo_curr_loc)
            houses.add(tuple(robo_curr_loc))

    return len(houses)


def main():
    with open('data/day3.txt', 'r') as f:
        data = f.read()

    print 'Number of houses Santa visits alone = {}'.format(santa_alone(data))
    print 'Number of houses Santa and Robo visit = {}'.format(robo_santa(data))


if __name__ == '__main__':
    main()
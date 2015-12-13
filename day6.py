
def get_coordinate_pair(instruction):
    remove_start = instruction.strip('turn on').strip('toggle').strip('turn off')
    start_pair_str, end_pair_str = remove_start.strip().split('through')
    start_pair = map(lambda x: int(x), start_pair_str.split(','))
    end_pair = map(lambda x: int(x), end_pair_str.split(','))
    return start_pair, end_pair

def make_lighting_grid():
    lighting_grid = [[0 for col in range(1000)] for row in range(1000)]
    with open('data/day6.txt', 'r') as f:
        for line in f:
            start, end = get_coordinate_pair(line)
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    if line.startswith('turn on'):
                        lighting_grid[x][y] += 1

                    elif line.startswith('toggle'):
                        lighting_grid[x][y] += 2
                        # if lighting_grid[x][y] == 1:
                        #     lighting_grid[x][y] = 0
                        # else:
                        #     lighting_grid[x][y] = 1

                    else:
                        if lighting_grid[x][y] > 0:
                            lighting_grid[x][y] -= 1

    num_lit = 0
    for row in lighting_grid:
        for col in row:
            num_lit += col
    return num_lit


if __name__ == "__main__":
    print 'number of lights = {}'.format(make_lighting_grid())
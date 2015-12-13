import itertools


def parse_line_data(line):
    split_line = line.split()
    person = split_line[0]
    neighbor = split_line[len(split_line)-1].strip('.')
    hu = int(split_line[3])
    change = split_line[2]
    if change == 'lose':
        hu = -hu
    return person, {neighbor: hu}

def calculate_happiness():
    happiness_options = {}
    with open('data/day13.txt', 'r') as f:
        for line in f:
            person_name, neighbor_dict = parse_line_data(line)
            if person_name in happiness_options:
                happiness_options[person_name].update(neighbor_dict)
            else:
                happiness_options[person_name] = neighbor_dict

    seating_plans = {}
    guest_list = happiness_options.keys()

    # Add yourself to the guest list
    happiness_options['me'] = {}
    guest_list.append('me')
    for happiness_option in happiness_options:
        if happiness_option != 'me':
            happiness_options[happiness_option]['me'] = 0
            happiness_options['me'][happiness_option] = 0

    for seating_plan in itertools.permutations(guest_list, len(guest_list)):
        happiness = 0
        for guest_num, guest in enumerate(seating_plan):
            if guest_num < len(seating_plan)-1:
                neighbor = seating_plan[guest_num+1]
            else:
                neighbor = seating_plan[0]
            happiness += happiness_options[guest][neighbor]
            happiness += happiness_options[neighbor][guest]
        seating_plans[happiness] = seating_plan

    return max(seating_plans.keys())


if __name__ == "__main__":
    print 'max happiness = {}'.format(calculate_happiness())
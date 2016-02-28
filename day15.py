import itertools


def get_flavor_traits(flavor):
    name, attributes = flavor.split(":")

    flavor_dict = {name: {}}
    for attribute in attributes.split(","):
        attr_name, attr_amt = attribute.split()
        flavor_dict[name][attr_name] = attr_amt

    return flavor_dict


def get_best_cookie(flavor_data):
    ingredient_list = flavor_data.keys()


def main():
    flavor_data = {}
    with open('data/day15.txt', 'r') as f:
        for line in f:
            flavor_data.update(get_flavor_traits(line))

    print 'The total score of the highest scoring cookie is {}'.format(get_best_cookie(flavor_data))


if __name__ == "__main__":
    main()



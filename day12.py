import json


TEST_CASES = [
    dict(
        a=10,
        b=[1,2,3]
    )
]


def sum_numbers():
    num_sum = 0
    with open('data/day12.txt', 'r') as f:
        data = json.load(f)

    final_sum = _recurse_sum(data)

    print "Final answer: {}".format(final_sum)

    for each in TEST_CASES:
        val = _recurse_sum(each)
        print 'Test [[{!r}]] => {}'.format(each, val)

    return num_sum

def _recurse_sum(val):
    if isinstance(val, dict):
        return sum(_recurse_sum(v) for v in val.itervalues())
    elif isinstance(val, int):
        return val
    elif isinstance(val, list):
        return sum(_recurse_sum(v) for v in val)
    elif isinstance(val, basestring):  # unicode|str
        return 0
    else:
        print "Unknown type! {!r}".format(val)



if __name__ == "__main__":
    print 'sum of all numbers = {}'.format(sum_numbers())
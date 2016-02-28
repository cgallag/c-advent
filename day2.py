
def amt_wrapping_paper(box_inputs):
    return sum(calculate_wrapping_paper(box) for box in box_inputs)

def calculate_wrapping_paper(box):
    l, w, h = map(int, box.split('x'))
    ordered_sides = sorted([l, w, h])
    return 2*l*w + 2*w*h + 2*h*l + ordered_sides[0]*ordered_sides[1]

def amt_ribbon(box_inputs):
    return sum(calculate_ribbon(box) for box in box_inputs)

def calculate_ribbon(box):
    l, w, h = map(int, box.split('x'))
    bow = l*w*h

    ordered_sides = sorted([l, w, h])
    sides = 2*ordered_sides[0] + 2*ordered_sides[1]

    return bow + sides

def main():
    data = []
    with open('data/day2.txt', 'r') as f:
        for line in f:
            data.append(line)

    print 'Total sq ft wrapping paper = {}'.format(amt_wrapping_paper(data))
    print 'Total ft ribbon = {}'.format(amt_ribbon(data))


if __name__ == "__main__":
    main()
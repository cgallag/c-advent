import re


# (1) It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# (2) It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# (3) It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
def is_nice_string(input_str):
    patterns = [
        r'.*[aeiou].*[aeiou].*[aeiou].*',
        r'(\w)\1',
        r'^(a(?!b)|[^a])*$',
        r'^(c(?!d)|[^c])*$',
        r'^(p(?!q)|[^p])*$',
        r'^(x(?!y])|[^x])*$',

    ]
    for pattern in patterns:
        if not re.search(pattern, input_str):
            return False
        else:
            print '{} passed for {}'.format(input_str, pattern)

    # Only return true if the string matches all three patterns
    return True

def count_nice_strings(is_new=False):
    num_nice = 0
    with open('data/day5.txt', 'r') as f:
        for line in f:
            if is_new:
                pass
            elif is_nice_string(line.strip()):
                num_nice +=1
    return num_nice


if __name__ == "__main__":
    print '# nice strings = {}'.format(count_nice_strings())
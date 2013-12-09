import itertools
import operator

def checkio(data):
    current = []
    for row in data:
        extended = map(max, zip([0] + current, current + [0]))
        current = list(itertools.starmap(operator.add, zip(extended, row)))
        print 'extended: {}, current: {}'.format(extended, current) 
    return max(current)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1],
        [2, 3],
        [3, 3, 1],
        [3, 1, 5, 4],
        [3, 1, 3, 1, 3],
        [2, 2, 2, 2, 2, 2],
        [5, 6, 4, 5, 6, 4, 3]
    ]) == 23, "First example"
    assert checkio([
        [1],
        [2, 1],
        [1, 2, 1],
        [1, 2, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 2, 1, 1, 1, 1],
        [1, 2, 1, 1, 1, 1, 9]
    ]) == 15, "Second example"
    assert checkio([
        [9],
        [2, 2],
        [3, 3, 3],
        [4, 4, 4, 4]
    ]) == 18, "Third example"
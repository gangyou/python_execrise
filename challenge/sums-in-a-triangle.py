def checkio(data):
    opt = [[ 0 for j in range(i+1)] for i in range(len(data))]

    for i in range(len(data)):
        if i ==0:
            opt[0][0] = data[0][0]
            continue

        for j in range(i+1):
            if j == 0:
                opt[i][j] = data[i][j] + opt[i-1][j]
            elif j == i:
                opt[i][j] = data[i][j] + opt[i-1][j-1]
            else:
                opt[i][j] = data[i][j] + max(opt[i-1][j-1], opt[i-1][j])

    return max(opt[-1])

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
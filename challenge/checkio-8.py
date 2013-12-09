def checkio(game_result):
	for i, line in enumerate(game_result):
		for j, ch in enumerate(line):
			if is_win(i, j, ch, game_result): return ch

	return 'D'


def is_win(x, y, sign, game_result):
	if game_result[x][y] == '.':
		game_result[x][y] = sign

	# check end condition
	# check col
	for i in range(3):
		if game_result[x][i] != sign: break
		if i == 2: return True

	# check row
	for i in range(3):
		if game_result[i][y] != sign: break
		if i == 2: return True

	# check diag
	if(x == y):
		# We're on diagonal
		for i in range(3):
			if game_result[i][i] != sign: break;
			if i == 2: return True

if __name__ == '__main__':
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"



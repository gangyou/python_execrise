from collections import deque

d = deque('ghi')
print [ x.upper() for x in d]

d.append('j')
d.appendleft('f')
print d

assert d.pop() == 'j'
assert d.popleft() == 'f'
assert list(d) == list('ghi')
assert 'h' in d
d.extend('jkl')
assert list(d) == list('ghijkl')
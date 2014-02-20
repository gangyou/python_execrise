# coding:utf8

import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())

count = {}

for word in words:
    times = count.get(word, 0)
    count[word] = times + 1

print sorted(count.items(), lambda x, y: cmp(y[1], x[1]))[:10]
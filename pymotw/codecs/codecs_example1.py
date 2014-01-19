#-*- encoding:gb2312 -*-
import codecs, sys

print '-' * 60

look = codecs.lookup('gb2312')
look2 = codecs.lookup('utf-8')

a = '我爱北京天安门'

print len(a), a
b = look.decode(a)

print b[1], b[0], type(b[0])
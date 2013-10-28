# coding=utf8
import re

text = "a line of text\\012another line of text\\012etc..."

def octal(match):
	return chr(int(match.group(1), 8))

octal_pattern = re.compile(r"\\(\d\d\d)")

print text

# 给Sub指定一个回调函数，处理
print octal_pattern.sub(octal, text)
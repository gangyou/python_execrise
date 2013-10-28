import re

text = "you're no fun anymore..."

print re.sub("fun", "entertaining", text)

print re.sub("[^\w]+", "-", text)

print re.sub("\S+", "-BEEP-", text)


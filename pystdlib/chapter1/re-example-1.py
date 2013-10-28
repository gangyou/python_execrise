import re

text = "The Attile the Hun Show"

m = re.match(".", text)
if m : print repr("."), "=>", repr(m.group(0))

m = re.match(".*", text)
if m : print repr(".*"), "=>", repr(m.group(0))

m = re.match("\w+", text)
if m : print repr("\w+"), "=>", repr(m.group(0))

m = re.match("\d+", text)
if m : print repr("\d+"), "=>", repr(m.group(0))
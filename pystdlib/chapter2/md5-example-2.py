import md5, string, base64

hash = md5.new()
hash.update("spam, spam, and eggs")

value = hash.digest()
print hash.hexdigest()

print base64.encodestring(value)
import pickle

data = {
	'foo': [1,2,3],
	'bar': ('Hello', 'World!'),
	'baz': True
}

jar = open('data.pkl', 'wb')
pickle.dump(data, jar)
jar.close()

pkl_file = open('data.pkl', 'rb')
data = pickle.load(pkl_file)
print data
pkl_file.close()
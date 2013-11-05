import tempfile

tf = tempfile.TemporaryFile()

for i in range(100):
	tf.write("*" * 100)

# removes the file
tf.close()

import os

print "File exists? : ", os.path.exists(str(tf))
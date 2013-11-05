import tempfile, os

named_temp_file = tempfile.NamedTemporaryFile(delete=True)

print named_temp_file.name

print "File exists? :", os.path.exists(str(named_temp_file))

named_temp_file.close()

print "File exists? :", os.path.exists(str(named_temp_file))
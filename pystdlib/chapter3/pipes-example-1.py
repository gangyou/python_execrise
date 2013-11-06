import pipes

t = pipes.Template()

# create a pipeline
t.append("sort", "--")
t.append("uniq", "--")

# filter some text
t.copy("../chapter2/samples/sample.txt", "")


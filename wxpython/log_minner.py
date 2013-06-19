import re

match_log = re.compile(r"^\[.*SystemOut.*\[flowTrace\]\[(.*start.*)\]$")
result = {}
print "mining log"
with open("SystemOut.log") as log:
	for line in log:
		print ".",
		mo = match_log.match(line)
		if mo:
			data = mo.group(1)
			infos = data.split(",")
			infos = map(lambda x: x.strip(), infos)
			flow_name = infos[3]
			op_name = infos[4]
			if flow_name in result: 
				result[flow_name] += 1	
			else: result[flow_name] = 1

with open("result.log", "w") as reslog:
	for key,value in result.items():
		reslog.write(key + " : " + str(value) + "\n")

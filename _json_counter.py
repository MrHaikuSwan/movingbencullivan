import os, json
counter = 0
for fname in os.listdir('.')[1:]:
	with open(fname) as f:
		counter += len(json.load(f))
print(counter)
input('Press ENTER to quit')
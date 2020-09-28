import os, json
counter = 0
for fname in sorted(os.listdir('.'))[1:]:
	with open(fname) as f:
		try:
			data = json.load(f)
		except Exception:
			data = []
		counter += len(data)
print(counter)
input('Press ENTER to quit')
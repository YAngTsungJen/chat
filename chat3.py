lines = []
with open("3.txt", "r", encoding = "utf-8-sig") as f:
	for line in f:
		lines.append(line.strip())
for line in lines:
	s = line.split(" ")
	time = s[0][:5]
	name = s[0][5:]
	print(time, name)
import os, sys

input1 = ""
input2 = ""
output = ""

for i in range(len(sys.argv)):
    if sys.argv[i] == "-i":
        input1 = sys.argv[i+1]
        input2 = sys.argv[i+2]
    elif sys.argv[i] == "-o":
        output = sys.argv[i+1]

if not (os.path.exists(input1) and os.path.exists(input2)):
    input("One or more input files does not exist. Press any key to exit")
    sys.exit()

if not ((input1).ends(".txt") and (input2).endswith(".txt")):
    input("One or more input files is not a TXT file. Press any key to exit")
    sys.exit()

lines = []
positions = []

f1 = open(input1, "r")
for line in f1:
    if not line.startswith(">"):
        lines.append(line)

f1.close()

for pos in lines[0]:
    if lines[0][pos] == "-":
        positions.append(pos)

headers = []
edit = []

f2 = open(input2, "r")
for line in f2:
    if line.startswith(">"):
        headers.append(line)
    else:
        edit.append(line)

for count in range(len(pos)):
    for j in range(len(edit)):
        edit[j] = edit[j][:count] + "-" + edit[j][count:]

fo = open(output, "w")

for k in range(len(headers)):
    fo.write(headers[k])
    fo.write(chars[k])

fo.close()
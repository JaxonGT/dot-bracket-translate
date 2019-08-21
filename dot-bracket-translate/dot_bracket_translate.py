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
    sys.exit(0)

if not ((input1).endswith(".txt") and (input2).endswith(".txt")):
    input("One or more input files is not a TXT file. Press any key to exit")
    sys.exit(0)

lines = []
positions = []
headers = []
edit = []

f1 = open(input1, "r")
for line in f1:
    if not line.startswith(">"):
        lines.append(line)

f1.close()

f2 = open(input2, "r")
for line in f2:
    if line.startswith(">"):
        headers.append(line)
    else:
        edit.append(line)

f2.close()

if not "-" in lines[0] or not "." in edit[0]:
    input("Input 1 should contain unknowns. Input 2 should contain dot-brackets. Press any key to exit")
    sys.exit(0)

for pos in range(len(lines[0])):
    if lines[0][pos] == "-":
        positions.append(pos)

for count in range(len(positions)):
    for j in range(len(edit)):
        edit[j] = edit[j][:positions[count]] + "-" + edit[j][positions[count]:]

fo = open(output, "w")

for k in range(len(headers)):
    fo.write(headers[k])
    fo.write(edit[k])

fo.close()
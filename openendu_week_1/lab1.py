import re

inp = open('input.txt', 'r')
out = open('output.txt', 'w')

s = 0

f = inp.read()
f = re.split(r' ', f)
f = [int(i) for i in f]

for x in f:
    s += x

out.write(str(s))

inp.close()
out.close()
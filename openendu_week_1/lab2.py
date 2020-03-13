import re

inp = open('input.txt', 'r')
out = open('output.txt', 'w')

f = inp.read()
f = re.split(r' ', f)
f = [int(i) for i in f]

s = f[0] + f[1] ** 2
out.write(str(s))

inp.close()
out.close()
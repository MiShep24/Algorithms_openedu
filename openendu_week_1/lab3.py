import re

inp = open('input.txt', 'r')
out = open('output.txt', 'w')

f = inp.read()
f = re.split(r' ', f)
n = f[0].splitlines()
f.remove(f[0])
f = n + f
n = int(f.pop(0))
f = [int(i) for i in f]
a = list()
for i in range(n):
    j = i - 1
    key = f[i]
    while f[j] > key and j >= 0:
        f[j+1] = f[j]
        j -= 1
    f[j+1] = key
    a.append(j+2)
a = [str(i) for i in a]
f = [str(i) for i in f]
out.write(' '.join(a) + '\n' + ' '.join(f))

inp.close()
out.close()

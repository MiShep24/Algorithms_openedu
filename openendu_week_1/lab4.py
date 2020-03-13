import re


def qsort(arr):
    if arr:
        a = [x for x in arr if x < arr[0]]
        print(a)
        b = [x for x in arr if x == arr[0]]
        print(b)
        c = [x for x in arr if x > arr[0]]
        print(c)
        return qsort(a) + b + \
               qsort(c)
    return []


inp = open('input.txt', 'r')
out = open('output.txt', 'w')

f = inp.read()
f = re.split(r' ', f)
n = f[0].splitlines()
f.remove(f[0])
f = n + f
n = int(f.pop(0))
f = [float(i) for i in f]
c = [*f]
m = qsort(f)
print(m)

for i in range(n):
    if c[i] == m[0]:
        min = i + 1
    if c[i] == m[n // 2]:
        av = i + 1
    if c[i] == m[n - 1]:
        max = i + 1

out.write(str(min) + ' ' + str(av) + ' ' + str(max))

inp.close()
out.close()

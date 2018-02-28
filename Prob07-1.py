
import fileinput


# x[n+1] = C + (A * x[n] + M) / (B * x[n] + N)
def nextx(x, c, a, m, b, n):
    return c + (a * x + m) / (b * x + n)


def process(line):
    x, a, b, c, m, n, e = map(float, line.split())

    if e < 0:
        e = -e

    for i in xrange(0, 100):
        newx = nextx(x, c, a, m, b, n)
        diff = newx - x
        if -e < diff and diff < e:
            return "{:.6f}".format(newx)
        x = newx
    return "DIVERGES"


count = None
for line in fileinput.input():
    if not count:
        count = int(line)
        continue
    print process(line)
    count = count - 1

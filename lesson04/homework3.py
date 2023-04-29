f = open('data.txt', 'r')
f1 = open('result.txt', 'w')
for line in f:
    fizz, buzz, N = map(int, line.split())
    res = ''
    for i in range(1, N + 1):
        if i % fizz:
            if i % buzz:
                res += f'{i} '
            else:
                res += 'B '
        elif i % buzz:
            res += 'F '
        else:
            res += 'FB '
    f1.write(res+'\n')
f.close()
f1.close()

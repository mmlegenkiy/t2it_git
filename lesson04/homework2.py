f = open('data.txt', 'r')
for line in f:
    fizz, buzz, N = map(int, line.split())
    for i in range(1, N + 1):
        if i % fizz:
            if i % buzz:
                print(i, end=' ')
            else:
                print("B", end=' ')
        elif i % buzz:
            print("F", end=' ')
        else:
            print("FB", end=' ')
    print()
f.close()

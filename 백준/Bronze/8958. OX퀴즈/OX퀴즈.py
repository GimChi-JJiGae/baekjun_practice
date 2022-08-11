T = int(input())

for t in range(T):
    ox = input()
    oxli = []
    ocnt = 0
    for o in ox:
        if o == 'O':
            ocnt += 1
            oxli.append(ocnt)
        else:
            ocnt = 0
    print(sum(oxli))
n =input()

while len(n) != 0:
    a = n[:10]
    n = n[10:]
    for j in a:
        print(j,end='')
    print()
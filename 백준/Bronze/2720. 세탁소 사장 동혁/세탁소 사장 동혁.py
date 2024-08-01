T = int(input())

for i in range(T):
    arr = []
    C = int(input())
    arr.append(C//25)
    C = C%25
    arr.append(C//10)
    C = C%10
    arr.append(C//5)
    C = C%5
    arr.append(C//1)
    for j in arr:
        print(j, end=" ")
testcase = 10


def in_order(n):
    if n:
        in_order(ch1[n])
        print(node_name[n], end="")
        in_order(ch2[n])


def find_root(v):
    for i in range(1, v + 1):
        if par[i] == 0:
            return i

for tc in range(1, testcase + 1):
    V = int(input())  # 정점 개수, 마지막 정점번호
    E = V - 1
    node_name = [0] * (V + 1)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    par = [0] * (V + 1)

    for i in range(V):
        temp = list(input().split())
        node_name[int(temp[0])] = temp[1]
        if len(temp) == 3:
            ch1[int(temp[0])] = int(temp[2])
            par[int(temp[2])] = int(temp[0])
        elif len(temp) == 4:
            ch1[int(temp[0])] = int(temp[2])
            ch2[int(temp[0])] = int(temp[3])
            par[int(temp[2])] = int(temp[0])
            par[int(temp[3])] = int(temp[0])

    root = find_root(V)
    print(f"#{tc}", end=" ")
    in_order(root)
    print()
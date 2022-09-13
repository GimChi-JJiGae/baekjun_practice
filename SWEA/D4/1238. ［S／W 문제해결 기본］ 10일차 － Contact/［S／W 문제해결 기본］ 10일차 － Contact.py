

testcase = 10
for tc in range(1, testcase + 1):

    length, start = map(int, input().split())

    arr = list(map(int, input().split()))

    V = {}
    for i in range(100):
        V[i + 1] = []

    distance = [0]*101

    for i in range(len(arr) // 2):
        V[arr[i*2]].append(arr[i*2 + 1])

    que = [start]

    while que:
        node = que.pop(0)
        for next in V[node]:
            if distance[next]:
                continue
            else:
                que.append(next)
                distance[next] = distance[node] + 1

    max_distance = 0
    max_distance_index = 0
    for i in range(101):
        if distance[i] >= max_distance:
            max_distance = distance[i]
            max_distance_index = i


    print(f"#{tc} {max_distance_index}")



def dfs(start, route, N):

    stack = [start]
    visited = [0 for i in range(N+1)]


    while(stack):
        node = stack.pop()
        if not visited[node]:
            print(node, end=" ")
            visited[node] = 1
        else:
            continue
        try:
            for w in route[node]:
                stack.append(w)
        except KeyError:
            continue
    print()
    return


def bfs(start, route, N):

    queue = [start]
    visited = [0 for i in range(N+1)]
    visited[start] = 1

    while(queue):
        node = queue.pop(0)
        print(node, end=" ")
        try:
            for w in route[node]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = 1
                else:
                    continue
        except KeyError:
            continue
    print()
    return


N, M, V = map(int, input().split())
route1 = {}
route2 = {}
for i in range(N):
    route1[i + 1] = []
    route2[i + 1] = []
for i in range(M):
    start, end = map(int, input().split())
    route1[start].append(end)
    route1[end].append(start)
    route2[start].append(end)
    route2[end].append(start)
for i in range(N):
    route1[i + 1].sort()
    route2[i + 1].sort(reverse=True)

dfs(V, route2, N)
bfs(V, route1, N)



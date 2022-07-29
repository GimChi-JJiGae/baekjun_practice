N = int(input())
Big_paper = [[0 for j in range(100)] for i in range(100)]

point_list = [[0, 0] for i in range(N)]
for i in range(N):
    point_list[i][0], point_list[i][1] = map(int, input().split())

for i in range(N):
    for j in range(point_list[i][0] -1, point_list[i][0] -1 + 10):
        for k in range(point_list[i][1] - 1, point_list[i][1] -1 + 10):
            Big_paper[j][k] = 1


count = 0
for i in range(100):
    for j in range(100):
        if Big_paper[i][j] == 1:
            count += 1

print(count)
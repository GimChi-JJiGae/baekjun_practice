arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))
# 값 하나씩 탐색하며 최댓값을 찾는다.
max_value = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_value:
            max_value = arr[i][j]
            row = i+1
            col = j+1

print(max_value)
print(row, col)
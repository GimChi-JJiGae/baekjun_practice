max_val = 0
row = 0
col = 0
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] >= max_val:
            row = i + 1
            col = j + 1
            max_val = arr[j]
print(max_val)
print(row, col)
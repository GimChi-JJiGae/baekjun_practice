
testcase = int(input())
for tc in range(1, testcase + 1):
    N = int(input())
    print(f"#{tc}")
    pascal = [[] for i in range(N)]
    length = 1
    for i in range(N):
        for j in range(length):
            if j == 0 or j == length - 1:
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        length += 1
        print(*pascal[i])



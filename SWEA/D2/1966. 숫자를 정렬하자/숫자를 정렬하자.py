
testcase = int(input())

for tc in range(1, testcase + 1):

    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(1, N):
        for j in range(i):
            if numbers[i] < numbers[j]:         # 삽입정렬, 자기 앞에 자기 보다 작은 값이 있다면 그자리로 옮긴다.
                numbers.insert(j, numbers[i])   # 삽입 시켜서 값을 집어넣음
                numbers.pop(i + 1)              # 추가적으로 삽입 시킨 형태이므로 원래 있던 값은 원래 위치에서 제거
    print(f"#{tc}", end=' ')
    print(*numbers)
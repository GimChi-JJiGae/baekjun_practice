
test_case = int(input())

for tc in range(test_case):
    N = int(input())
    carrots = list(map(int, input().split()))
    count = 1
    max_count = 1
    for i in range(N - 1):                      # 인덱스를 신경써서 N - 1 까지만 for문을 돈다.
        if carrots[i] < carrots[i + 1]:         # 다음 원소가 커지는지 확인
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1

    print(f"#{tc + 1} {max_count}")





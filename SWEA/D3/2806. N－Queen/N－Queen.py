def Queens(floor ,checked, we_can, n):
    global total
    if floor == n:
        total += 1

    for i in range(len(we_can)):                    # 우리가 뽑을 수 있는 것중
        cannot = False
        for j in range(len(checked)):   # 이미 한 것의 대각선에 걸리면 안된다.
            if checked[j] + (floor - j) == we_can[i] or checked[j] - (floor - j) == we_can[i]:
                cannot = True
                break
        if cannot:
            continue

        Queens(floor + 1, checked + [we_can[i]], we_can[:i] + we_can[i + 1:], n)

testcase = int(input())

for tc in range(1, testcase + 1):
    N = int(input())

    if N == 1:
        print(f"#{tc} 1")
        continue
    if N == 2:
        print(f"#{tc} 0")
        continue

    total = 0
    arr = list(range(N))
    Queens(0, [], arr, N)
    print(f"#{tc} {total}")
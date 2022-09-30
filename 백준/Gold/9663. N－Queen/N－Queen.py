def Queens(floor ,checked, we_can, n):
    global total
    if floor == n:      # 끝까지 순열을 다 만들 수 있으면 +1 해준다
        total += 1

    for i in range(len(we_can)):                        # 우리가 뽑을 수 있는 것중
        cannot = False
        for j in range(len(checked)):                   # 이미 한 것의 대각선에 걸리면 안된다.
            if checked[j] + (floor - j) == we_can[i] or checked[j] - (floor - j) == we_can[i]:
                cannot = True
                break
        if cannot:
            continue

        Queens(floor + 1, checked + [we_can[i]], we_can[:i] + we_can[i + 1:], n)

N = int(input())
total = 0
arr = list(range(N))
Queens(0, [], arr, N)
print(f"{total}")
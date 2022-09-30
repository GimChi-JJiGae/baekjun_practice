def Queens(floor, checked, we_can, n):
    global total

    if floor == n:      # 끝까지 순열을 다 만들 수 있으면 +1 해준다
        total += 1

    if floor == 0:

        tmp = len(we_can) // 2 # 절반만 진행하면 된다.

        for i in range(tmp):  # 우리가 뽑을 수 있는 것중

            cannot = False
            for j in range(len(checked)):  # 이미 한 것의 대각선에 걸리면 안된다.
                if checked[j] + (floor - j) == we_can[i] or checked[j] - (floor - j) == we_can[i]:
                    cannot = True
                    break
            if cannot:
                continue

            Queens(floor + 1, checked + [we_can[i]], we_can[:i] + we_can[i + 1:], n)


    else:
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


if N % 2:
    odd = True
else:
    odd = False

total = 0
temp = 0
arr = list(range(N))
Queens(0, [], arr, N)
total = total * 2
if odd:                     # 홀수일 경우 중간에 있는 값만 빼고 구한 후 * 2, 이후에 중간에 있는 값만 넣고 계산한 후 더해준다.
    temp += total
    total = 0
    Queens(1, [N//2], arr[:N//2] + arr[N//2 + 1:], N)
    total += temp
print(total)
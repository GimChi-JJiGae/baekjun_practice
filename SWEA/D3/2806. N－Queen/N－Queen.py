import copy

def Queens(floor ,checked, we_can, n):
    global total
    if floor == n:
        total += 1

    for i in we_can:                    # 우리가 뽑을 수 있는 것중
        cannot = False
        for j in range(len(checked)):   # 이미 한 것의 대각선에 걸리면 안된다.
            if checked[j] + (floor - j) == i or checked[j] - (floor - j) == i:
                cannot = True
                break
        if cannot:
            continue
        new_checked = copy.deepcopy(checked)
        new_we_can = copy.deepcopy(we_can)
        new_checked.append(i)
        new_we_can.remove(i)
        Queens(floor + 1, new_checked, new_we_can, n)

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
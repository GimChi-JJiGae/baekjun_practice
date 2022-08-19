
testcase = int(input())

for tc in range(1, testcase + 1):
    num = int(input())

    money = list(map(int, input().split()))
    result = 0
    day = 0
    while(True):

        max_val = max(money)
        max_day = money.index(max_val)
        for i in range(max_day):
            result += max_val - money[i]

        money = money[max_day + 1:]
        if len(money) == 0:
            break

    print(f"#{tc} {result}")



testcase = int(input())

for tc in range(1, testcase + 1):
    num = int(input())

    money = list(map(int, input().split()))
    result = 0
    day = 0
    while(True):

        max_val = max(money)                    # 가장 비쌀 때의 값
        max_day = money.index(max_val)          # 가장 비싼 날
        for i in range(max_day):
            result += max_val - money[i]        # 0번 인덱스부터 가장 비싼 날까지 값의 차이를 모두 합함

        money = money[max_day + 1:]             # 가장 비싼날 앞부분은 모두 자름
        if len(money) == 0:                     # 잘랐을 때 리스트 길이가 0이되면 종료
            break

    print(f"#{tc} {result}")


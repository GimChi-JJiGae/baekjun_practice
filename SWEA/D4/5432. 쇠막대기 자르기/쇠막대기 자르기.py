
testcase = int(input())

for tc in range(1, testcase + 1):
    blank_list = list(input())

    result = 0                                      # 결과적으로 만들어지는 쇠막대 수
    bar_count = 0                                   # 전체 쇠막대수를 카운트하기 위한 변수
    count = 0                                       # 현재 위치에 올려져 있는쇠막대 수를 카운트
    for i in range(len(blank_list)):
        if blank_list[i] == "(":
            if blank_list[i + 1] == ")":            # 레이저 위치일 경우 지금까지의 count를 결과값에 더함, 레이저가 자른 쇠막대만큼 쇠막대수가 늘어나므로
                result += count
            else:
                count += 1                          # 레이저가 아닐경우 쇠막대가 하나 더 올라온 것임
                bar_count += 1
        elif blank_list[i] == ")":
            if blank_list[i - 1] == "(":            # 레이저였을 경우 그냥 지나감
                continue
            else:
                count -= 1                          # 올려져 있던 쇠막대를 지나간 것임
    result += bar_count                             # 결과값 = 레이저가 자른 횟수 + 기존 쇠막대 수
    print(f"#{tc} {result}")




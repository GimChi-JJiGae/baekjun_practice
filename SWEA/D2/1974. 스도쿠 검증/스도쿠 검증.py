
testcase = int(input())
for tc in range(1, testcase + 1):
    result = -1
    v = [[] for i in range(9)]
    for a in range(3):
        box = [[] for b in range(3)]                    # 세로 라인 표현을 위한 리스트 만들기
        for i in range(3):
            line_ = list(map(int, input().split()))
            for j in range(9):
                v[j].append(line_[j])
            if sum(line_) != 45:                        # 가로 합체크
                result = 0
            for j in range(3):
                box[j] = box[j] + line_[3*j:3*(j+1)]    # 3x3 박스 만들기

        for i in range(3):
            for j in range(9):
                if box[i].count(j + 1) != 1:            # 3x3 박스 안에 한개씩 들어가 있는지를 체크
                    result = 0
                    break
            if result == 0:
                break

        for i in range(3):
            if sum(box[i]) != 45:                       # 3x3 박스의 합 체크
                result = 0
                break
                
    for i in range(9):                                  # 세로 길이 합 체크
        if sum(v[i]) != 45:
            result = 0
            break



    if result != 0:
        result = 1

    print(f"#{tc} {result}")

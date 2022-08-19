
testcase = int(input())


for tc in range(1, testcase + 1):
    result = -1
    v = [[] for i in range(9)]
    for a in range(3):
        box = [[] for b in range(3)]
        for i in range(3):
            line_ = list(map(int, input().split()))
            for j in range(9):
                v[j].append(line_[j])
            if sum(line_) != 45:

                result = 0
            for j in range(3):
                box[j] = box[j] + line_[3*j:3*(j+1)]


        for i in range(3):
            for j in range(9):
                if box[i].count(j + 1) != 1:
                    result = 0

                    break
            if result == 0:
                break

        for i in range(3):
            if sum(box[i]) != 45:
                result = 0

                break
    for i in range(9):
        if sum(v[i]) != 45:
            result = 0
            break



    if result != 0:
        result = 1

    print(f"#{tc} {result}")

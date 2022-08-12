
test_case = int(input())

for tc in range(1, test_case + 1):
    length = int(input())
    numbers = input()           # int로 바꾸지 말자 0이 앞에 있다.

    max_count = 0
    count = 0
    for i in range(length):
        if numbers[i] == '1':   # 1인지 확인하면 count 증가
            count += 1
            if count > max_count:   # 최댓값을 갱신하는지 확인
                max_count = count
        else:
            count = 0           # 1이 아니면 count를 0으로 초기화

    print(f"#{tc} {max_count}")

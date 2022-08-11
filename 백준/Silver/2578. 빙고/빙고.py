import sys

input = sys.stdin.readline

my_board = []                                           # 나의 빙고판
call_number = []                                        # 사회자가 부른 숫자 1차원 배열
my_board_for_search = []                                # 사회자가 부른 숫자 검색용 1차원 배열

for i in range(5):
    my_board.append(list(map(int, input().split())))
    for j in range(5):
        my_board_for_search.append(my_board[i][j])
for i in range(5):
    a = list(map(int, input().split()))
    for j in range(5):
        call_number.append(a[j])


call_count = 0                                          # 나중에 print할 사회자가 몇 번째 숫자를 불렀는지 카운트
for i in range(len(call_number)):
    bingo = 0
    for j in range(len(my_board_for_search)):
        if my_board_for_search[j] == call_number[i]:
            idx = j
            break

    call_count += 1

    pos_i = idx // 5
    pos_j = idx % 5

    my_board[pos_i][pos_j] = 'a'                    # 불려진 숫자 체크

    if i >= 11:                                     # 3빙고가 나는 최소 조건
        for row in range(5):                          # 가로 빙고가 있는지 확인
            if my_board[row].count('a') == 5:
                bingo += 1

        for col in range(5):
            count = 0
            for row in range(5):
                if my_board[row][col] == 'a':
                    count += 1
            if count == 5:
                bingo += 1

        count = 0
        for cross in range(5):
            if my_board[cross][cross] == 'a':
                count += 1
        if count == 5:
            bingo += 1
        count = 0
        for cross in range(5):
            if my_board[cross][4 - cross] == 'a':
                count += 1
        if count == 5:
            bingo += 1
        count = 0

    if bingo >= 3:
        break
print(call_count)




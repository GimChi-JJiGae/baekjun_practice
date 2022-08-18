
testcase = int(input())

for tc in range(1, testcase + 1):
    words = [[] for i in range(5)]
    max_len = 0
    for i in range(5):
        word = input()
        for j in range(len(word)):
            words[i].append(word[j])                # 한글자씩 리스트에 append한다
        if len(words[i]) > max_len :
            max_len = len(words[i])

    print(f"#{tc}", end=" ")
    for j in range(max_len):
        for i in range(5):
            try:
                print(words[i][j], end="")          # 실행이 되는 부분은 출력됨
            except IndexError:
                continue                            # 가장 긴 부분을 제외한 나머지 부분은 인덱스가 넘어가도 그냥 넘어감
    print()



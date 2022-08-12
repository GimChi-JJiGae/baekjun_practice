
test_case = 10

for i in range(1, test_case + 1):
    tc = int(input())
    checking_word = input()
    s = input()

    count = 0

    for j in range(len(s) - len(checking_word) + 1):        # 긴 문자열 s를 돌면서
        for k in range(len(checking_word)):                 # 짧은 문자열과 비교하여 짧은 문자열이 들어있는지 확인한다.

            if s[j + k] != checking_word[k]:                # 아니라면 break
                break
        else:                                               # checking_word가 온전히 다 들어있다면
            count += 1

    print(f"#{tc} {count}")



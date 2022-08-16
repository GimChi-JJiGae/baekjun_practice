
test_case = int(input())
for tc in range(1, test_case + 1):
    A, B = input().split()
    A_len = len(A)
    B_len = len(B)
    result = A_len                      # 초기에는 A 길이만큼 타이핑 해야한다.

    skip = 0
    for i in range(A_len - B_len + 1):
        if skip:
            skip -= 1
            continue
        for j in range(B_len):
            if A[i + j] != B[j]:
                break
        else:
            result -= (B_len - 1)   # B를 사용하면 되므로 B의길이 -1 만큼 덜 타이핑해도 된다
            skip = B_len - 1        # B가 있음을 확인했으므로 B가 끝날 때까지는 비교를 안해도 된다

    print(f"#{tc} {result}")

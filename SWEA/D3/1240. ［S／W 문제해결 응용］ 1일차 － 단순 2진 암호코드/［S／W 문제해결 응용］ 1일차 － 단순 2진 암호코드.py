testcase = int(input())

code_num = {0: "0001101",
            1: "0011001",
            2: "0010011",
            3: "0111101",
            4: "0100011",
            5: "0110001",
            6: "0101111",
            7: "0111011",
            8: "0110111",
            9: "0001011"}

for tc in range(1, testcase + 1):
    N, M = map(int, input().split())

    for i in range(N):              # N개의 라인을 받아야하지만 우리는 1이 들어있는 라인만 찾으면된다
        temp = list(input())
        for j in range(len(temp)):
            if temp[j] == "1":
                arr = temp[:]
                break
        else:
            continue                # 1을 발견 못하면 계속돌자

    start_idx = 0
    end_idx = 0

    for i in range(len(arr)):
        if arr[i] == "1":
            start_idx = i
            break
    for j in range(len(arr) - 1, -1, -1):
        if arr[j] == "1":
            end_idx = j
            break

    length = end_idx - start_idx + 1            # 처음 1이 나오는 곳에서 마지막 1이 나오는 곳
    need_zero = 56 - length                     # 처음 1앞에는 부족한 길이만큼 0을 넣어줘야한다.
    code = ''.join(arr[start_idx:end_idx+1])
    code = "0" * need_zero + code

    translated = [0, 0, 0, 0, 0, 0, 0, 0]
    odd_sum = 0
    even_sum = 0
    

    for i in range(8):                              # 56글자라고 했으므로..
        for j in range(10):
            if code[i*7:i*7 + 7] == code_num[j]:    # 암호 코드와 비교해본다.
                translated[i] = j
                break
        if (i + 1) % 2:
            odd_sum += translated[i]
        else:
            even_sum += translated[i]
    #print(f"#{tc} {code}")
    #print(f"#{tc} {translated}")



    if (odd_sum * 3 + even_sum) % 10 == 0:
        print(f"#{tc} {sum(translated)}")
    else:
        print(f"#{tc} 0")








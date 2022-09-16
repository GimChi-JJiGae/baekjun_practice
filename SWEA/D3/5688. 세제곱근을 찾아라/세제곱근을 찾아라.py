
testcase = int(input())

for tc in range(1, testcase + 1):
    N = int(input())
    temp = int((N**(1/3)))
    for i in range(temp, temp + 2):
        if i**3 == N:
            print(f"#{tc} {i}")
            break
    else:
        print(f"#{tc} -1")

testcase = int(input())

for tc in range(1, testcase + 1):
    total, bundle = map(int, input().split())
    f = total // bundle
    d = total % bundle
    bundles = [f for i in range(bundle)]
    i = 0
    while(d != 0):
        bundles[i] += 1
        i += 1
        d -= 1
    result = 1
    for i in range(len(bundles)):
        result = result * bundles[i]

    print(f"#{tc} {result}")
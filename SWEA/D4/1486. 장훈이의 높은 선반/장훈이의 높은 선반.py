
def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result


testcase = int(input())
for tc in range(1, testcase + 1):
    num, target = map(int, input().split())
    people = list(map(int, input().split()))

    least_gap = target

    for i in range(1, len(people) + 1):
        comb_result = comb(people, i)

        for j in comb_result:
            if sum(j) >= target:
                gap = sum(j) - target
                if least_gap > gap:
                    least_gap = gap

    print(f"#{tc} {least_gap}")


from itertools import combinations

testcase = int(input())


def calc_taste(list_):
    global matrix

    result = 0

    a = list(combinations(list_, 2))
    for b in a:

        result = result + matrix[b[0]][b[1]] + matrix[b[1]][b[0]]

    return result


for tc in range(1, testcase + 1):
    N = int(input())

    matrix = [None] * N

    ingredients = list(range(N))                            # 재료 리스트
    full_set = set(ingredients)

    min_gap = 20000 * 16 * 16                               # 식재료 시너지 차이는 이를 넘을 수 없음

    for i in range(N):
        matrix[i] = list(map(int, input().split()))

    comb = list(combinations(ingredients, N // 2))          # 재료 조합 튜플들의 리스트


    for j in range(len(comb)//2):
        set1 = set(comb[j])                                 # 세트로 만든 재료조합들
        set2 = full_set - set1                              # 남은 재료들로 만든 세트

        list1 = list(set1)                                  # 다시 리스트로
        list2 = list(set2)

        gap = abs(calc_taste(list2) - calc_taste(list1))

        if min_gap > gap:
            min_gap = gap

    print(f"#{tc} {min_gap}")








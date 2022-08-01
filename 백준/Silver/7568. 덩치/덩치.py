def compare(a, b):
    if a[0] > b[0]:
        if a[1] > b[1]:
            return 1 # a가 덩치가 큰 경우
    if a[0] < b[0]:
        if a[1] < b[1]:
            return 2 # b가 덩치가 큰 경우 , 문제에서는 자기보다 덩치가 큰 사람 수가 등수로 이어지므로 이 결과가 필요
    return 3 # 덩치가 비교불가능한 경우

n = int(input())
result = []
humans =[[0,0] for i in range(n)]

for i in range(n): # 주어진 데이터를 먼저 2차원 배열안에 집어넣는다.
    w, h = map(int, input().split())
    for j in range(2):
        humans[i][0] = w
        humans[i][1] = h

scores= dict()
for i in range(n):
    scores[i] = 0 # n개의 칸을 갖는 배열 초기화


for i in range(len(humans)): # compare 함수를 이용하여 각자 자기보다 덩치큰 사람이 몇명인지 확인한다.
    count = 0
    for j in range(len(humans)):
        if humans[i] == humans[j]:
            continue
        else:
            if compare(humans[i], humans[j]) == 2:
                count += 1
    scores[i] = count # 딕셔너리에 값을 저장



ranking = list(scores.values())

for i in range(len(ranking)):
    ranking[i] = ranking[i] + 1 # 0등 부터 시작하므로 1씩 올린다.
    print(ranking[i], end=' ')


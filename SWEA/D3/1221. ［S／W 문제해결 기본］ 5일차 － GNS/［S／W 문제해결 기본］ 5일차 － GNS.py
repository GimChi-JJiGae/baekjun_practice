
test_case = int(input())

a_to_num = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}

num_to_a = {0 : 'ZRO', 1 : 'ONE', 2 : 'TWO', 3 : 'THR', 4 : 'FOR', 5 : 'FIV', 6 : 'SIX', 7 : 'SVN', 8 : 'EGT', 9 : 'NIN'}

for tc in range(test_case):
    numbering, length = input().split()

    length = int(length)


    numbers = list(input().split())

    for i in range(len(numbers)):
        numbers[i] = a_to_num[numbers[i]]           # 딕셔너리를 이용해 int로 변경

    numbers.sort()                                  # 정렬

    for i in range(len(numbers)):
        numbers[i] = num_to_a[numbers[i]]           # 딕셔너리를 이용해 다시 문자열로 변경



    print(numbering)
    print(*numbers)                                 # output 메모장 예시와 달리 이렇게만 해도 정답 취급임



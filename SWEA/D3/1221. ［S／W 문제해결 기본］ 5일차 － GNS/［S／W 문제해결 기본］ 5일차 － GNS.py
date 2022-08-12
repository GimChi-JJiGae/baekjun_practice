
test_case = int(input())

a_to_num = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}

num_to_a = {0 : 'ZRO', 1 : 'ONE', 2 : 'TWO', 3 : 'THR', 4 : 'FOR', 5 : 'FIV', 6 : 'SIX', 7 : 'SVN', 8 : 'EGT', 9 : 'NIN'}

for tc in range(test_case):
    numbering, length = input().split()

    length = int(length)

    numbers = []
    while(len(numbers) < length):                   # 여러줄로 입력되고 있으므로 총 길이에 해당하는 값이 될 때까지 계속 입력받자
        numbers = numbers + list(input().split())

    for i in range(len(numbers)):
        numbers[i] = a_to_num[numbers[i]]           # 딕셔너리를 이용해 int로 변경

    numbers.sort()                                  # 정렬

    for i in range(len(numbers)):
        numbers[i] = num_to_a[numbers[i]]           # 딕셔너리를 이용해 다시 문자열로 변경



    print(numbering)
    print(*numbers)



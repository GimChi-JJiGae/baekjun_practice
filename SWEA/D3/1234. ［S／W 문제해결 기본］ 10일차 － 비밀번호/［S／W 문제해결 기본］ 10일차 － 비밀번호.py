class Stack:
    def __init__(self):                             # 스택 생성자
        self._data = []

    def __len__(self):
        return len(self._data)                      # 스택 크기 반환

    def push(self, e):
        self._data.append(e)                        # 스택에 e를 추가함

    def is_empty(self):
      return len(self._data) == 0                   # 스택이 비어있으면 True를 반환함. 비어있다면 len(self._data) == 0 이 True 값임

    def pop(self):                                  # pop 명령
        if self.is_empty():                         # 만약 비어있다면 None을 반환
            return None
        return self._data.pop()                     # 리스트에서 pop한 것을 반환

    def top(self):
        if self.is_empty():                         # 만약 비어있다면 None을 반환
            return None
        return self._data[-1]                       # 가장 마지막에 있는 값을 반환, 반환만 하고 값을 없애진 않음

# 문제 해결 아이디어 : 하노이의 탑
# stack1의 내용물이 stack2로 온전히 옮겨지면 종료
testcase = 10

for tc in range(1, testcase + 1):

    length, words = input().split()
    words = list(words)

    stack1 = Stack()
    stack2 = Stack()



    for i in range(len(words)):
        stack1.push(words[i])                       # 스택1에 주어진 문자열 한글자씩 집어넣음

    while(True):
        len1 = stack1.__len__()                     # 검사 시작전 스택1의 길이를 잰다

        while(not stack1.is_empty()):               # 스택1이 비워질때까지 비교한다
            stack2.push(stack1.pop())               # 스택2에 하나를 집어넣고

            if stack2.top() == stack1.top():        # 스택1의 top과 스택2의 top이 같은지 비교한다
                stack1.pop()                        # 같다면 연속 중복 문자이므로 제거한다
                stack2.pop()
            else:
                continue
        len2 = stack2.__len__()                     # 검사 후 스택2의 길이를 잰다
        if len1 == len2:                            # 검사 후의 스택2의 길이가 처음의 스택1의 길이와 같다면 중복이 없는 것이므로 종료
            break
        else:
            while(not stack2.is_empty()):
                stack1.push(stack2.pop())           # 다시 한번 while문을 돌기 위하여 스택2의 내용물을 스택 1에 옮긴다

    result = ''
    while(not stack2.is_empty()):
        result = result + stack2.pop()


    print(f'#{tc} {result}')
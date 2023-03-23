def check(answer):
    # answer: 현재까지 설치된 기둥과 보의 정보를 담은 리스트
    for x, y, a in answer:
        # 기둥인 경우
        if a == 0:
            # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나 다른 기둥 위에 있어야 합니다.
            if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        # 보인 경우
        elif a == 1:
            # 보는 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    # answer: 현재까지 설치된 기둥과 보의 정보를 담은 리스트
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        # b가 0인 경우 삭제, 1인 경우 설치
        if b == 0:
            answer.remove([x, y, a])
            # 구조물을 삭제한 후에도 올바른 구조물인지 검사합니다.
            if not check(answer):
                answer.append([x, y, a])
        elif b == 1:
            answer.append([x, y, a])
            # 구조물을 설치한 후에도 올바른 구조물인지 검사합니다.
            if not check(answer):
                answer.remove([x, y, a])
    # x좌표, y좌표, 기둥인지 보인지 기준으로 정렬합니다.
    answer.sort()
    return answer
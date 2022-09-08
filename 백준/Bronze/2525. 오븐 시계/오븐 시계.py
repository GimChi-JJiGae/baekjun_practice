H, M = map(int, input().split())
N = int(input())

plus_H = N // 60
plus_M = N % 60

H = H + plus_H
M = M + plus_M

if M >= 60:
    H = H + 1
    M = M - 60
else:
    pass

if H >= 24:
    H -= 24

print(H, M)

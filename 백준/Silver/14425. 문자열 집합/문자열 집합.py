import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dic = {}
count = 0

for i in range(N):
  dic[input().rstrip()] = 0

for i in range(M):
  if input().rstrip() in dic:
    count += 1

print(count)
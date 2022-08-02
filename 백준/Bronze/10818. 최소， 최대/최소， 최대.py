N = int(input())
result = list(map(int, input().split()))
result.sort()
print(result[0], result[-1])
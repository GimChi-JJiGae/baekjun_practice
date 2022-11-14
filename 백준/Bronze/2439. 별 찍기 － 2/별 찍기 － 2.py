N = int(input())
for i in range(N):
    result = "" + " "*(N - (i + 1)) + "*"*(i + 1)
    print(result)
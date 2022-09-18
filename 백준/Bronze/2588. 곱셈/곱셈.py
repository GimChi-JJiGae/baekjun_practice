a = int(input())
b = int(input())

temp = b % 10
print(a*temp)


temp = (b // 10) % 10

print(a*temp)

temp = (b // 100)

print(a*temp)

print(a*b)

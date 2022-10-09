cnt_list = [0]*42

for i in range(10):
    tmp = int(input())
    cnt_list[tmp%42] = cnt_list[tmp%42] + 1

cnt = 0
for j in range(42):
    if cnt_list[j] != 0:
        cnt += 1
print(cnt)
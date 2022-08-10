n = int(input())

for i in range(n):
    k = int(input())
    n = int(input())
    li = []
    li2 = []
    for j in range(1, n+1):
        li.append(j)
    for s in range(k):
        for x in range(1,n+1):
            li2.append(sum(li[:x]))
        li = li2[:]
        li2=[]
    print(li[-1])
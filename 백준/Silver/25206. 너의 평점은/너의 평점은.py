score_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
s = 0
s_c = 0
cnt = 0
check = 0
while (check < 20):
    check += 1
    name, point, score = input().split()

    if (score == "P"):
        continue
    else:
        cnt += 1
        s += float(point) * score_dict[score]
        s_c += float(point)
val = s / s_c
print("{:.6f}".format(val))

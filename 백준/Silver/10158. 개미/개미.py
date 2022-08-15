import sys
input = lambda: sys.stdin.readline().strip()

w, h = map(int, input().split())
pos_x, pos_y = map(int, input().split())

t = int(input())


if w - pos_x >= t:
    pos_x = pos_x + t
else:
    tx = t - (w - pos_x)
    move_w = tx // w
    x_d = tx % w
    if move_w % 2 == 0:
        pos_x = w - x_d
    else:
        pos_x = x_d

if h - pos_y >= t:
    pos_y = pos_y + t
else:
    ty = t - (h - pos_y)
    move_h = ty // h
    y_d = ty % h
    if move_h % 2 == 0:
        pos_y = h - y_d
    else:
        pos_y = y_d

print(pos_x, end=' ')
print(pos_y)



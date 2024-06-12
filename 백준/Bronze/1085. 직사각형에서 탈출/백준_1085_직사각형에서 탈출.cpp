#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int x, y, w, h;
    int min_d = 1001;
    int tmp1, tmp2, tmp3;
    cin >> x >> y >> w >> h;
    tmp1 = w - x;
    tmp2 = x;
    min_d = min(tmp1, tmp2);
    tmp3 = min(h - y, y);
    min_d = min(min_d, tmp3);
    cout << min_d;

    return 0;
}
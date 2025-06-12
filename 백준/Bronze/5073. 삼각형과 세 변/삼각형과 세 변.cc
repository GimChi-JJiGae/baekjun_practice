#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c;

    while (true) {
        cin >> a >> b >> c;

        if (a == 0 && b == 0 && c == 0) break;

        int sides[3] = {a, b, c};
        sort(sides, sides + 3); // 오름차순 정렬

        if (sides[0] + sides[1] <= sides[2]) {
            cout << "Invalid" << endl;
        } else if (sides[0] == sides[1] && sides[1] == sides[2]) {
            cout << "Equilateral" << endl;
        } else if (sides[0] == sides[1] || sides[1] == sides[2] || sides[0] == sides[2]) {
            cout << "Isosceles" << endl;
        } else {
            cout << "Scalene" << endl;
        }
    }

    return 0;
}

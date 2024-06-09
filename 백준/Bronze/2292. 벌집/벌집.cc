#include <iostream>

using namespace std;


int main() {

    int n = 1;
    int now = 1;
    int target;
    cin >> target;
    while (target > now + 6 * n) {
        now = now + 6 * n;
        n++;
    }
    if (target == 1) {
        cout << 1;
    }
    else {
        cout << n + 1;
    }
    

    return 0;
}
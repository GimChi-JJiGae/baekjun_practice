#include <iostream>
#include <string>
using namespace std;

bool threeSixes(long long number) {
    string tmp_str = to_string(number);
    int count = 0;
    for (char ch : tmp_str) {
        if (ch == '6') {
            count++;
            if (count == 3) return true;
        } else {
            count = 0;
        }
    }
    return false;
}

int main() {
    int N;
    cin >> N;
    int k = 0;
    long long now = 666;

    while (k < N) {
        if (threeSixes(now)) {
            k++;
        }
        now++;
    }

    cout << now - 1;
    return 0;
}
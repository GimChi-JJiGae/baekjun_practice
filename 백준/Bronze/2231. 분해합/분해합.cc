#include <iostream>
using namespace std;

int getDigitSum(int num) {
    int sum = num;
    while (num > 0) {
        sum += num % 10; 
        num /= 10;
    }
    return sum;
}

int main() {
    int n;
    cin >> n;

    int result = 0;
    for (int i = max(1, n - 9 * 7); i < n; i++) {  
        if (getDigitSum(i) == n) {
            result = i;
            break;
        }
    }

    cout << result << endl;
    return 0;
}
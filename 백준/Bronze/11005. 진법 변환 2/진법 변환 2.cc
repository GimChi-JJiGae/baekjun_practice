#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {

    int N, B;
    vector<char> result;
    scanf("%d %d", &N, &B);

    int p = 0;

    while (1) {
        int pow_val_check = pow(B, p);
        //cout << pow_val_check << " " << p << endl;
        if (N / pow_val_check > 0) {
            p = p + 1;
        }
        else {
            break;
        }
    }

    int tmp = N;

    for (int i = p; i >= 0; i--) {
        //cout << p << endl;
        
        int pow_val = pow(B, i);
        int tmp_val = tmp / pow_val;    // 몫
        char char_val; // 집어넣을 값
        if (tmp_val < 10) {
            char_val = (char)(tmp_val + 48);
        }
        else {
            char_val = (char)(tmp_val + 55);
        }
        tmp = tmp % pow_val;
        result.push_back(char_val);
    }

    for (int i = 1; i < result.size(); i++) {
        cout << result[i];
    }

    return 0;
}
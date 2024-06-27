#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<double> scores;
    int N;
    double tmp;
    double best = -1;
    double sum_s = 0;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        scores.push_back(tmp);
        sum_s += tmp;
        if (best < tmp) {
            best = tmp;
        }
    }

    cout << (sum_s / best * 100) / N;


}
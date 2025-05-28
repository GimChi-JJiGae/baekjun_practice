#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);  // C++ 스트림 동기화 비활성화
    cin.tie(NULL);                // cin과 cout 분리

    int N;
    cin >> N;
    vector<pair<int, int>> v(N);

    for (int i = 0; i < N; i++) {
        cin >> v[i].first >> v[i].second;
    }

    sort(v.begin(), v.end());  

    for (const auto& p : v) {
        cout << p.first << " " << p.second << "\n"; 
    }

    return 0;
}
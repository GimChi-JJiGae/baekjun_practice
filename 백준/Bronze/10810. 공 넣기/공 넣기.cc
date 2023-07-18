#include <iostream>

using namespace std;

int main() {
    int N;
    int M;
    int arr[101] = { 0 };
    cin >> N;
    cin >> M;
    for (int i = 0; i < M; i++) {
        int start, end, num;
        cin >> start;
        cin >> end;
        cin >> num;

        for (int j = 0; j < end - start + 1; j++) {
            arr[j + start] = num;
        }
    }
    for (int k = 0; k < N; k++) {
        cout << arr[k + 1] << " ";
    }
}
#include <iostream>

using namespace std;

int main() {
    int N, M, a, b;
    
    int tmp;
    cin >> N >> M;
    int* arr = new int[N + 1];
    for (int i = 0; i < N + 1; i++) {
        arr[i] = i;
    }
    for (int i = 0; i < M; i++) {
        cin >> a >> b;
     
        for (int j = 0; j <= (b - a)/2; j++) {
            tmp = arr[b - j];
            
            arr[b - j] = arr[a + j];
            arr[a + j] = tmp;
            
        }
    }
    for (int i = 1; i < N + 1; i++) {
        cout << arr[i] << " ";
    }



    return 0;
}
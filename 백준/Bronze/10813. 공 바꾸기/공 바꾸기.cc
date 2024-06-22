#include <iostream>

using namespace std;

int main(){
    
    int N, M;
    int a, b, tmp;
    int* arr = new int[N + 1];
    for(int i = 1; i < N + 1; i++){
        arr[i] = i;
    }
    
    cin >> N >> M;
    for(int i = 0; i < M; i++){
        cin >> a >> b;
        tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
    
    for(int i = 1; i < N + 1; i++){
        cout << arr[i] << " ";
    }
    
    delete[] arr;
    
    return 0;
}
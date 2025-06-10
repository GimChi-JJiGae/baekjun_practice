#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);  
    cin.tie(NULL);   
    
    int N, M;
    int arr[100001];
    int tmp;
    cin >> N >> M;
    arr[0] = 0;
    for(int i = 1; i < N + 1; i++){
        cin >> tmp;

        arr[i] = arr[i - 1] + tmp;
        
    }
    
    int s, e;

    for (int i = 0; i < M; i++){
        cin >> s >> e;
        
        cout << arr[e] - arr[s - 1] << "\n";
    }

    return 0;
}
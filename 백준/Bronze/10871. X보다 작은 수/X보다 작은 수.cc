#include <iostream>

using namespace std;

int main() {
    int N;
    int X;
    cin >> N;
    cin >> X;
    
    for (int i = 0; i < N; i++){
        int tmp;
        cin >> tmp;
        if(tmp < X){
            cout << tmp << " ";
        }
    }
}
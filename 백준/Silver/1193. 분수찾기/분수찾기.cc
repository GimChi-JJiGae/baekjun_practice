#include <iostream>
#include <string>
using namespace std;

int main(){
    int X, N;
    N = 1;
    cin >> X;
    
    while(N * (N + 1) / 2 < X){
        N += 1;
    }
    
    int s = N * (N - 1) / 2;
    int num_left = X - s;
    string front = to_string(N + 1 - num_left);
    string back = to_string(num_left);
    if (N % 2){
        cout << front << "/" << back;
        }
    else{
        cout << back << "/" << front;
        }

    return 0;
}
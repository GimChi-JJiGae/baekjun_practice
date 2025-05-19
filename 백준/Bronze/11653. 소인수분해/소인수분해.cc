#include <iostream>
using namespace std;

int main(){
    int N, n;
    cin >> N;
    n = 2;

    
    if (N == 1){
        return 0;
    }
    
    while(N >= n && N != 1){
        if(N % n == 0){
            N = N / n;
            cout << n << endl;
        } else{
            n += 1;
        }
    }
    
    
    
    return 0;
}
#include <iostream>
using namespace std;

int main(){
    int a1, a0, c, n0;
    int n_val, num_val;
    cin >> a1 >> a0;
    cin >> c;
    cin >> n0;
    n_val = c - a1;
    if (n_val >= 0){
        if (a0 <= n_val * n0){
            cout << 1;
        } else{
            cout << 0;
        }
    } else {
    
        cout << 0;
    }
    
    
    
    return 0;
}
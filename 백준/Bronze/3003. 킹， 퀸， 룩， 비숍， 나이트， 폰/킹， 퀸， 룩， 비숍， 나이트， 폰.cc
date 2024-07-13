#include <iostream>

using namespace std;

int main(){
    
    int k, q, r, b, kn, p;
    int K = 1;
    int Q = 1;
    int R = 2;
    int B = 2;
    int KN = 2;
    int P = 8;
    
    cin >> k >> q >> r >> b >> kn >> p;
    cout << K - k << " " << Q - q << " " << R - r << " " << B - b << " " << KN - kn << " " << P - p;
    return 0;
}
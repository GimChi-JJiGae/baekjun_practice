#include <iostream>
using namespace std;
int main(){
    int d = 2;
    int n;
    cin >> n;
    
    while(n--){
        d = d * 2 - 1;
    }
    
    cout << d * d;
    
    return 0;
}
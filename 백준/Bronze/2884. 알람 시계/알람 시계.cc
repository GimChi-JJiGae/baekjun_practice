#include <iostream>

using namespace std;

int main(){
    
    int A, B;
    int new_A, new_B;
    bool need_hour_minus = false;
    cin >> A >> B;
    if(B >= 45){
        new_B = B - 45;
    } else{
        new_B = B + 15;
        need_hour_minus = true;
    }
    if(need_hour_minus){
        if(A == 0){
            new_A = 23;
        } else {
            new_A = A - 1;
        }
    } else{
        new_A = A;
    }
    cout << new_A << " " << new_B;
    
    return 0;
}
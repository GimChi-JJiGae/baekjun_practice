#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int A, B, V;
    int pre_target;
    int days;
    scanf("%d %d %d", &A, &B, &V);
    
    if(V - A <= 0){
        cout << 1;
    } else{
        pre_target = V - A;
        days = pre_target / (A - B);
        if (pre_target % (A - B) != 0){
            days += 1;
        }
        days += 1;
        cout << days;
    }
    
    
    
    return 0;
}
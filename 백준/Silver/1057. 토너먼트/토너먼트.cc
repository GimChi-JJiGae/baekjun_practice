#include <iostream>

using namespace std;


int main(){
    
    int N, A, B;
    int round = 1;
    cin >> N >> A >> B;
    while(true){
        if((A+1) / 2 == (B+1) / 2){
            if(A < B){
                if(A % 2 == 1){
                    break;
                }
            } else{
                if(B % 2 == 1){
                    break;
                }
            }
        }
        A = (A + 1) / 2;
        B = (B + 1) / 2;
        round += 1;
        
    }
    
    cout << round;

    
    return 0;
}
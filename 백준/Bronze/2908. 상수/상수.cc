#include <iostream>
#include <string>

using namespace std;

int main(){
    int a, b;
    string A, B;
    cin >> a >> b;
    string new_A, new_B;
    new_A = "";
    new_B = "";
    A = to_string(a);
    B = to_string(b);
    for(int i = 0; i < 3; i++){
        new_A.push_back(A[2 - i]);
        new_B.push_back(B[2 - i]);
    }
    
    a = stoi(new_A);
    b = stoi(new_B);
    if(a > b){
        cout << a;
    } else{
        cout << b;
    }
    
    return 0;
}
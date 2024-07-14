#include <string>
#include <iostream>

using namespace std;

int main(){
    string s;
    int length, half;
    
    cin >> s;
    length = s.size();
    half = length / 2;
    
    bool p = true;
    
    for(int i = 0; i < half; i++){
        if(s[i] != s[length - 1 - i]){
            p = false;
            break;
        }
    }
    if(p){
        cout << 1;
    } else{
        cout << 0;
    }
    
    
    return 0;
}
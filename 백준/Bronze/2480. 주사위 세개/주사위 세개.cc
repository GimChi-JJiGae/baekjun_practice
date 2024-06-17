#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int a, b, c, reward=0;
    cin >> a >> b >> c;
    
    if (a==b && b==c){
        reward = 10000 + a*1000;
    }
    else if (a==b || a==c){
        reward = 1000 + a*100;
    }
    else if (b==c){ //같은 눈이 2개일 때
        reward = 1000 + b*100;
    }
    else {
        reward = max(max(a,b),c) * 100;
    }
    
    cout << reward;
    
    return 0;
} 
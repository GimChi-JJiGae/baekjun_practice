#include <iostream>
#include <string>

using namespace std;

int main(){
    char tmp_c;
    int N, tmp, s;
    string str;
    cin >> N;
    cin >> str;
    s = 0;
    
    
    
    for(int i = 0; i < N; i++){
        tmp_c = str[i];
        tmp = tmp_c - '0';
        s += tmp;
    }
    
    cout << s;
    
    return 0;
}
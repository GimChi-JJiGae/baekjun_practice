#include <iostream>
#include<vector>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    vector<vector<int>> v1(a, vector<int>(b));
    vector<vector<int>> v2(a, vector<int>(b));
    
    for(int i = 0; i < a; i++){
        for(int j = 0; j < b; j++){
            cin >> v1[i][j];
        }
    }
    
    for(int i = 0; i < a; i++){
        for(int j = 0; j < b; j++){
            cin >> v2[i][j];
        }
    }
    for(int i = 0; i < a; i++){
        for(int j = 0; j < b; j++){
            cout << v1[i][j] + v2[i][j] << ' '; 
        }
        cout << "\n";
    }
   
    return 0;
}
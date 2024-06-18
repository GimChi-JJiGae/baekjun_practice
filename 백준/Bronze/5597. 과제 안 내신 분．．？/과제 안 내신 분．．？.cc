#include <iostream>

using namespace std;

int main(){
    
    int students[31] ={0,};
    int tmp;
    for(int i = 1; i <= 28; i++){
        cin >> tmp;
        students[tmp] = 1;
    }
    
    for(int j = 1; j <= 30; j++){
        if(students[j] == 0){
            cout << j << endl;
        }
    }
    
    return 0;
}
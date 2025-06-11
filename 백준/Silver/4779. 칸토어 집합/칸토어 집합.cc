#include <iostream>
#include <cmath>

using namespace std;

void kantore(int num){
    
    if (num == 1){
        cout << "-";
    } else{
        int tmp;
        tmp = num / 3;
        
        kantore(tmp);
        for (int i = 0; i < tmp; i++){
            cout << " ";
        }
        kantore(tmp);
    }
}

int main(){
    double pow_num;
    int num;
    while (cin >> num){
        pow_num = pow(3, num);
        kantore(pow_num);
        cout << "\n";
    }
    
    return 0;
}
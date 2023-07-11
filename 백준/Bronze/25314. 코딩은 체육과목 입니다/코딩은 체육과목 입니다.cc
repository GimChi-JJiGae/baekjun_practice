#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    if (n == 4) {
        cout << "long int";
    } else {
        n = n - 4;
        for (int i = 0; i < n/4; i++){
            cout << "long ";
        }
        cout << "long int" << endl;
    }
    
    return 0;
    
}
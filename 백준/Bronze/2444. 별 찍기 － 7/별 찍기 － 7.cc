#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++){
        int j = n - i;
        int k = (n - j) * 2 - 1;
        while(j > 0){
            cout << " ";
            j--;
        }
        while(k > 0){
            cout << "*";
            k--;
        }
        cout << endl;
    }
    for(int i = 1; i < n; i++){
        int j = i;
        int k = (n - j) * 2 - 1;
        while(j > 0){
            cout << " ";
            j--;
        }
        while(k > 0){
            cout << "*";
            k--;
        }
        cout << endl;
    }
}
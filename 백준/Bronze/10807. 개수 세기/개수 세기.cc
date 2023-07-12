#include <iostream>

using namespace std;

int arr[101];

int main(){
    int N;
    int check;
    int count = 0;
    cin >> N;
    for (int i = 0; i < N; i++){
        int tmp;
        cin >> tmp;
        arr[i] = tmp;
    }
    cin >> check;
    for (int i = 0; i < N; i++){
        if (check == arr[i]){
            count++;
        }
    }
    cout << count;
}
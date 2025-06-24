#include <iostream>
using namespace std; 

int C = 0;

int fib(int n){

    if(n == 1 || n == 2){
        C++;
        return 1;
    } else{
        return (fib(n - 1) + fib(n - 2));
    }
}

int main(){
    int N, result;
    int arr[41] = {0};
    arr[1] = 1;
    arr[2] = 1;
 
    result = 0;
    cin >> N;
    fib(N);
    for(int i = 3; i <= N; i++){
        
        if (arr[i] != 0){
            continue;
        }
        else{
            arr[i] = arr[i - 1] + arr[i -2];
            result++;
        }
    }
    
    cout << C << " " << result;
    return 0;
}
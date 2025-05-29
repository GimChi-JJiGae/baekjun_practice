#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main(){
    int N, input, num;
    cin >> N;
    
    deque<pair<int, int>> dq;
    
    for (int i = 0; i < N; i++){
        cin >> input;
        dq.push_back({i, input});
    }
    
    while(!dq.empty()){
        auto now = dq.front();
        cout << now.first + 1 << " ";
        num = now.second;
        dq.pop_front();
        
        if(num > 0){
            num--;
            while(num != 0){
                dq.push_back(dq.front());
                dq.pop_front();
                num--;
            }
        } else {
            while(num != 0){
                dq.push_front(dq.back());
                dq.pop_back();
                num++;
            }
        }
    }
    return 0;
}
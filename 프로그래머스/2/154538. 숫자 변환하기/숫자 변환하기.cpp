#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int x, int y, int n) {
    int answer = -1;
    
    int arr[1000001] = {};
    
    if(x == y){
        return 0;
    }
    pair<int, int> first_pair = make_pair(x, 0);
    queue<pair<int, int>> q;
    q.push(first_pair);
    
    while(!q.empty()){
        int now_num, now_cnt;
        int tmp1, tmp2, tmp3;
        pair<int, int> now;
        now = q.front();
        now_num = now.first;
        now_cnt = now.second;
        // now_num = q.front().first();
        // now_cnt = q.front().second();
        q.pop();
        
        
        
        if(now_num == y){
            answer = now_cnt;
            break;
        }
        
        tmp1 = now_num + n;
        tmp2 = now_num * 2;
        tmp3 = now_num * 3;
        
        if (tmp1 <= y and arr[tmp1] == 0){
            auto new_pair1 = make_pair(tmp1, now_cnt + 1);
            arr[tmp1] = 1;
            q.push(new_pair1);
        }
        if (tmp2 <= y and arr[tmp2] == 0){
            auto new_pair2 = make_pair(tmp2, now_cnt + 1);
            arr[tmp2] = 1;
            q.push(new_pair2);
        }
        if (tmp3 <= y and arr[tmp3] == 0){
            auto new_pair3 = make_pair(tmp3, now_cnt + 1);
            arr[tmp3] = 1;
            q.push(new_pair3);
        }
        
    }
    return answer;
}
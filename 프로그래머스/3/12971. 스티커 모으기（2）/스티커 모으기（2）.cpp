#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int solution(vector<int> sticker)
{
    
    if(sticker.size() == 1){
        return sticker[0];
    }
    
    vector<int> dp(100001);
    
    // 0번을 뽑는 케이스
    
    dp[0] = sticker[0];
    dp[1] = max(sticker[0], sticker[1]);
    int answer =0;
    
    for(int i = 2; i < sticker.size() - 1; i++){
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1]);
    }
    
    answer = dp[sticker.size() - 2];
    
    // 0번을 안뽑는 케이스, 가장 뒤 인덱스가 사용가능
    
    dp[0] = 0;
    dp[1] = sticker[1];
    
    for(int i = 2; i < sticker.size(); i++){
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1]);
    }
    answer = max(answer, dp[sticker.size() - 1]);
    return answer;
}
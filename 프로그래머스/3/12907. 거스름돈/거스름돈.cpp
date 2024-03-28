#include <string>
#include <vector>

#include<iostream>
using namespace std;

int answer = 0;

int solution(int n, vector<int> money) {
    vector<int>dp(n+1,0);
    
    dp[0]=1;
    int tmp;
    
    for(int i = 0; i < money.size(); i++){     // 주어진 방법 수만큼 돌면서
        for(int j = 1; j < n+1; j++){           // n원까지 가면서
            tmp = 0;
            if( j >= money[i]){
                tmp = j - money[i];            // 남은 거스름돈
                dp[j] = dp[j] + dp[tmp];
            }
            else{
                continue;
            }
        }
    }
    
    return dp[n];
}


// #include <string>
// #include <vector>
// #include <algorithm>
// #include <iostream>
// using namespace std;

// const int INF = 987654321;

// const int MAX = 1e3 + 10;

// const int TEMPERATURE_RANGE = 50;

// int cache[MAX][TEMPERATURE_RANGE + 1];

// int solution(int temperature, int t1, int t2, int a, int b, vector<int> onboard) {
//     if (temperature >= t1 && t2 >= temperature)
//     {
//         return 0;
//     }
    
//     temperature += 10;
//     t1 += 10;
//     t2 += 10;
    
//     for (int i = 0; i < MAX; i++)
//     {
//         for (int j = 0; j <= TEMPERATURE_RANGE; j++)
//         {
//             cache[i][j] = INF;
//         }
//     }
    
//     cache[0][temperature] = 0;
    
//     for (int i = 0; i < onboard.size() - 1; i++)
//     {
//         for (int j = 0; j <= TEMPERATURE_RANGE; j++)
//         {
//             // 기저 사례: 손님이 탑승했을 때는 온도 조건을 충족해야 함
//             if (onboard[i] && 
//                (t1 > j || j > t2))
//             {
//                 continue;
//             }
            
//             int nextTemperature = j;
            
//             if (j < temperature && j < TEMPERATURE_RANGE)
//             {
//                 nextTemperature++;
//             }
//             else if (j > temperature && j > 0)
//             {
//                 nextTemperature--;
//             }
            
//             // 에어컨 껐을 때
//             cache[i + 1][nextTemperature] = min(cache[i + 1][nextTemperature], cache[i][j]);
            
//             // 에어컨을 켰고 온도 변화가 있을 때
//             if (j > 0)
//             {
//                 cache[i + 1][j - 1] = min(cache[i + 1][j - 1], a + cache[i][j]);
//             }
            
//             if (j < TEMPERATURE_RANGE)
//             {
//                 cache[i + 1][j + 1] = min(cache[i + 1][j + 1], a + cache[i][j]);
//             }
//             // 에어컨을 켰고 온도 변화가 있을 때
            
//             // 에어컨을 켰고 온도 유지 중일 때
//             cache[i + 1][j] = min(cache[i + 1][j], b + cache[i][j]);
//         }
//     }
    
//     int result = INF;
//     int len = onboard.size();

//     for (int j = 0; j <= TEMPERATURE_RANGE; j++)
//     {
//         if (onboard[len - 1] == 1 
//             && (t1 > j || j > t2))
//         {
//             continue;
//         }
        
//         result = min(result, cache[len - 1][j]);
//     }
    
//     return result;
// }

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int temperature, int t1, int t2, int a, int b, vector<int> onboard) {
    int answer = 0;
    vector<vector<int>> dp(onboard.size() + 1, vector<int>(55, 50*(a+b)*onboard.size()));
    
    
    if (temperature >= t1 && t2 >= temperature)
    {
        return 0;
    }
    
    t1 += 10;
    t2 += 10;
    temperature += 10;
    
    
    dp[0][temperature] = 0;
    
    for(int i = 0; i < onboard.size() - 1; i++){
        for(int j = 0; j <= 50; j++){
            if (onboard[i] && 
               (t1 > j || j > t2))
            {
                continue;
            }
            
            // 에어컨 안쓸경우
            
            int next_temper = j;
            
            if (j < temperature && j < 50){             // 끄면 자동으로 올라가는 경우
                next_temper++;
            } else if(j > temperature && j > 0){        // 내려가는 경우
                next_temper--;
            }
            
            dp[i + 1][next_temper] = min(dp[i + 1][next_temper], dp[i][j]);
            
            // 에어컨 쓸경우
            if(j > 0){
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j] + a);
            }
            
            if(j < 50){
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + a);
            }
            
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + b); // 에어컨으로 유지
         
        }
        
    }
    
    int min_energy = 50*(a+b)*onboard.size();
    
    for(int k = 0; k <= 50; k++){
        
        if(onboard[onboard.size() - 1] == 1 && (t2 < k || k < t1)){
            continue;
        }
        
        min_energy = min(min_energy, dp[onboard.size() - 1][k]);
    }
    
    // for(int i = 0; i < onboard.size(); i++){
    //     for(int j = 0; j < 3; j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    

    return min_energy;
}


// #include <string>
// #include <vector>
// #include <algorithm>

// using namespace std;

// // 에어컨은 현재온도 유지 or 희망온도로 위로 이동 or 희망온도 아래로 이동 or OFF(실외온도로 이동)

// void DFS(int temperature, int temper_now, int time, int t1, int t2, int a, int b, vector<int> &onboard, int energy, int &min_energy, vector<vector<int>> &dp){
    
//     if(dp[time][temper_now] < energy){
//         return;
//     } else{
//         dp[time][temper_now] = energy;
//     }
    
//     if(min_energy < energy){
//         return;                                 // 에너지 소비 이미 더 높음
//     }
    
//     if(time == onboard.size()){                 // 모든 시간 확인
//         min_energy = min(energy, min_energy);
//         return;
//     }
    
//     if(onboard[time] == 1){     // 승객이 있을 경우
//         if(temper_now < t1 || temper_now > t2){
//             return;            // 적정온도를 못맞추면 실패한 계획
//         } else {
//             DFS(temperature, temper_now, time + 1, t1, t2, a, b, onboard, energy + b, min_energy, dp); // 에어컨으로 현재 온도 유지 플랜
//             DFS(temperature, temper_now + 1, time + 1, t1, t2, a, b, onboard, energy + a, min_energy, dp); // 에어컨으로 온도올리기 플랜
//             DFS(temperature, temper_now - 1, time + 1, t1, t2, a, b, onboard, energy + a, min_energy, dp); // 에어컨으로 온도내리기 플랜
//             // 이하 에어컨 안쓰는 플랜
//             if(temperature > temper_now ){
//                 DFS(temperature, temper_now + 1, time + 1, t1, t2, a, b, onboard, energy, min_energy, dp);
//             } else if(temperature < temper_now){
//                 DFS(temperature, temper_now - 1, time + 1, t1, t2, a, b, onboard, energy, min_energy, dp);
//             } else{     // 실외랑 같을 때
//                 DFS(temperature, temper_now, time + 1, t1, t2, a, b, onboard, energy, min_energy, dp);
//             }
            
//         }
        
//     } else{                     // 승객이 없는 경우
//         DFS(temperature, temper_now, time + 1, t1, t2, a, b, onboard, energy + b, min_energy, dp); // 에어컨으로 현재 온도 유지 플랜
//         DFS(temperature, temper_now + 1, time + 1, t1, t2, a, b, onboard, energy + a, min_energy, dp); // 에어컨으로 온도올리기 플랜
//         DFS(temperature, temper_now - 1, time + 1, t1, t2, a, b, onboard, energy + a, min_energy, dp); // 에어컨으로 온도내리기 플랜
//         if(temperature > temper_now ){
//                 DFS(temperature, temper_now + 1, time + 1, t1, t2, a, b, onboard, energy, min_energy, dp);
//             } else if(temperature < temper_now){
//                 DFS(temperature, temper_now - 1, time + 1, t1, t2, a, b, onboard, energy, min_energy, dp);
//             } else{     // 실외랑 같을 때
//                 DFS(temperature, temper_now, time + 1, t1, t2, a, b, onboard, energy, min_energy, dp);
//             }
        
//     }
// }

// int solution(int temperature, int t1, int t2, int a, int b, vector<int> onboard) {
//     int answer = (a+b)*onboard.size();
//     vector<vector<int>> dp(onboard.size() + 1, vector<int>(55, answer));
//     DFS(temperature, temperature, 0, t1, t2, a, b, onboard, 0, answer, dp);
//     return answer;
// }
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>

//정답코드 출처 : https://howudong.tistory.com/334

using namespace std;

vector<vector<int>> node[50001]; // 연결 노드 정보
int dist[50001] = {0,}; // 각 노드의 최소 intensity
bool isTop[50001] = {false,}; // 그 노드가 산봉우리인지 체크
vector<int> ans(2); // 정답 배열

// 다익스트라
void dijkstra(vector<int> gates){
    // 우선순위 큐 intensity가 낮은게 가장 먼저 나오도록 설정
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> q;
    
    // 모든 출발지점 큐에 넣음
    for(auto it : gates){
        q.push({0,it}); // (intensity, 노드 번호)
        dist[it] = 0; // 출발 지점 = 0
    }
    
    while(!q.empty()){
        int x = q.top().second; // 현재 노드
        int cost = q.top().first; // 노드에 저장된 intensity
        q.pop();
        // ans에 값이 있고 최소 intensity가 현재 노드의 intensity보다 작은 경우
        if(ans[0] != -1 && ans[1] < cost) continue;
        // 해당 노드가 산봉우리인 경우
        if(isTop[x]){
            // 답에 저장된 intensity보다 작은 경우
            if(ans[0] == -1 || ans[1] > cost){
                // 갱신
                ans[0] = x;
                ans[1] = cost;
            }
            // 답에 저장된 intensity랑 같은데, 번호가 빠른 경우 번호만 바꿔줌
            else if(ans[1] == cost && ans[0] > x) ans[0] = x;
            continue;
        }
        
        // 현재 노드와 연결된 모든 노드 탐색
        for(int i = 0; i < node[x].size(); i++){
            int next = node[x][i][0];
            int nCost = node[x][i][1]; // 그 노드로 가는 비용
            nCost = max(nCost,cost); // 둘중 더 높은 비용
            
            // dist 배열에 저장된 비용보다 작은 경우
            if(dist[next] == -1 || nCost < dist[next]){
                // 갱신하고 큐에 넣음
                dist[next] = nCost;
                q.push({nCost,next});
            }
        }
    }
}

vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    for(auto it : summits) isTop[it] = true;
    fill(dist,dist+50001,-1); // dist 배열을 -1로 초기화
    ans[0] = -1;
    ans[1] = -1;
    
    // 노드 연결
    for(int i = 0; i < paths.size(); i++){
        int n1 = paths[i][0];
        int n2 = paths[i][1];
        int cost = paths[i][2];
        
        node[n1].push_back({n2,cost});
        node[n2].push_back({n1,cost});
    }
    dijkstra(gates);
    return ans;
}

// #include <string>
// #include <vector>
// #include <map>
// #include <iostream>

// using namespace std;

// void DFS(int& min_intensity, int& min_summit, map<int, vector<vector<int>>>& info, map<int, int>& where, map<int, int>& visited, int partial_min, int now, int start){
    
//     //cout << "현재위치 " << now << endl;
//     // 종점에 도달시
//     if(where[now] == 2){
//         if(partial_min < min_intensity){
//             min_summit = now;
//             min_intensity = partial_min;
//         } else if(partial_min == min_intensity) {
//             if(now < min_summit){
//                 min_summit = now;
//             }
//         }
//         return;
//     } else if(where[now] == 1 && now != start){ // 다른 출입구
//         return;
//     }
    
//     for(int i = 0; i < info[now].size(); i++){
//         int temp_intensity;
//         if(visited[info[now][i][0]] == 1){
//             continue;
//         }
//         if(info[now][i][1] > partial_min){
//             temp_intensity = info[now][i][1];
//         } else {
//             temp_intensity = partial_min;
//         }
//         if (temp_intensity > min_intensity){
//             continue;
//         }
//         visited[info[now][i][0]] = 1;
//         //cout << "다음 목표 " << info[now][i][0] << " 현재 최소 " << min_intensity << " 현재 최소 봉오리 " << min_summit << " 현재까지 intensity " << temp_intensity << endl; 
//         DFS(min_intensity, min_summit, info, where, visited, temp_intensity, info[now][i][0], start);
//         //cout << "후퇴 후 현 위치 " << now << endl;
//         visited[info[now][i][0]] = 0;
            
//     } 
// }

// vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
//     vector<int> answer;
    
//     int min_intensity = 10000001;
//     int min_summit = 50001;
    
//     map<int, vector<vector<int>>> info;
//     map<int, int> where;                // 게이트, 정상 정보, 0으로 초기화 되어있음
//     map<int, int> visited;              // 0은 방문 x
//     for(const auto& gate : gates){
//         where[gate] = 1;
//     }
//     for(const auto& summit : summits){
//         where[summit] = 2;
//     }
    
    
//     for(const auto& path : paths){
//         info[path[0]].push_back({path[1], path[2]});    // 이렇게만 해도되는듯
//         info[path[1]].push_back({path[0], path[2]});
//         // if(info.find(path[0]) != info.end()){
//         //     info[path[0]].push_back({path[1], path[2]});
//         // } else{
//         //     info[path[0]] = {{path[1], path[2]}};
//         // }
//     }
    
//     // 출입구별로 for 돌려서 시작해주자, visited 체크해주고
//     for(const auto& gate : gates){
    
//         visited[gate] = 1;
//         DFS(min_intensity, min_summit, info, where, visited, 0, gate, gate);
//         visited[gate] = 0;
//     }
//     answer.push_back(min_summit);
//     answer.push_back(min_intensity);
    
//     return answer;
// }